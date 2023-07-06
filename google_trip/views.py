from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.views.generic import ListView, DetailView
from .models import *
from .serializers import TouristAttractionSerializer, RestaurantSerializer, HotelSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class TouristAttractionsFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')
    # rating__lte = filters.NumberFilter(field_name='rating', lookup_expr='lte')
    class Meta:
        model = TouristAttraction
        fields = ['country__name', 'state__name', 'region__name', 'county__name', 'city__name', 'town__name', 'village__name', 'rating']

class HotelFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')
    # rating__lte = filters.NumberFilter(field_name='rating', lookup_expr='lte')
    class Meta:
        model = Hotel
        fields = ['country__name', 'state__name', 'region__name', 'county__name', 'city__name', 'town__name', 'village__name', 'rating']

class RestaurantFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')
    # rating__lte = filters.NumberFilter(field_name='rating', lookup_expr='lte')
    class Meta:
        model = Restaurant
        fields = ['country__name', 'state__name', 'region__name', 'county__name', 'city__name', 'town__name', 'village__name', 'rating']

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

class Geo(ListView):
    model = Country
    template_name = 'google_trip/geo.html'
    context_object_name = 'countries'
    # ordering = 'name'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hotels'] = Hotel.objects.filter(country='517').order_by('-number_of_review')[:3]
    #     context['tourist_attractions'] = TouristAttraction.objects.filter(country='517').order_by('-number_of_review')[
    #                                      :3]
    #     context['restaurants'] = Restaurant.objects.filter(country='517').order_by('-number_of_review')[:3]
    #     return context

class TouristAttractions(ListView):
    model = TouristAttraction
    context_object_name = 'tourist_attractions'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.GET.get('country__name')
        if country is None:
            return qs
        return qs.filter(country__name=country)


class Restaurants(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.GET.get('country__name')
        if country is None:
            return qs
        return qs.filter(country__name=country)


class Hotels(ListView):
    model = Hotel
    context_object_name = 'hotels'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.GET.get('country__name')
        if country is None:
            return qs
        return qs.filter(country__name=country)


class ViewAttraction(DetailView):
    model = TouristAttraction

class ViewRestaurant(DetailView):
    model = Restaurant


class ViewHotel(DetailView):
    model = Hotel


class APITouristAttractionsList(generics.ListCreateAPIView):
    queryset = TouristAttraction.objects.all().order_by('-number_of_review')
    serializer_class = TouristAttractionSerializer
    filterset_class = TouristAttractionsFilter
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
    filterset_class = RestaurantFilter


class APIHotelsList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all().order_by('-number_of_review')
    serializer_class = HotelSerializer
    filterset_class = HotelFilter