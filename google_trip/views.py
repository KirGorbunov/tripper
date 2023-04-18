from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.views.generic import ListView, DetailView
from .models import *
from .serializers import TouristAttractionSerializer, RestaurantSerializer, HotelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class Home(ListView):
    model = Country
    template_name = 'google_trip/index.html'
    context_object_name = 'countries'
    ordering = 'name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.filter(country='517').order_by('-number_of_review')[:3]
        context['tourist_attractions'] = TouristAttraction.objects.filter(country='517').order_by('-number_of_review')[
                                         :3]
        context['restaurants'] = Restaurant.objects.filter(country='517').order_by('-number_of_review')[:3]
        return context


class TouristAttractions(ListView):
    model = TouristAttraction
    context_object_name = 'tourist_attractions'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context


class Restaurants(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context


class Hotels(ListView):
    model = Hotel
    context_object_name = 'hotels'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context


class ViewAttraction(DetailView):
    model = TouristAttraction

class ViewRestaurant(DetailView):
    model = Restaurant


class ViewHotel(DetailView):
    model = Hotel


class APITouristAttractionsList(generics.ListCreateAPIView):
    queryset = TouristAttraction.objects.all().order_by('-number_of_review')
    serializer_class = TouristAttractionSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('country__name',)
    # def get_queryset(self):
    #     country = self.request.query_params.get('country')
    #     if country:
    #         return TouristAttraction.objects.order_by('-number_of_review').filter(country__name=country)[
    #                                      :3]
    #     else:
    #         return TouristAttraction.objects.all()


class APIRestaurantsList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().order_by('-number_of_review')
    serializer_class = RestaurantSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country__name',)


class APIHotelsList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all().order_by('-number_of_review')
    serializer_class = HotelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country__name',)