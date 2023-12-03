from rest_framework import generics
from django.views.generic import ListView, DetailView
from .models import TouristAttraction, Restaurant, Hotel, Country
from .serializers import TouristAttractionSerializer, \
    RestaurantSerializer, \
    HotelSerializer
from django_filters import rest_framework as filters
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class TouristAttractionsFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = TouristAttraction
        fields = ['country__name',
                  'state__name',
                  'region__name',
                  'county__name',
                  'city__name',
                  'town__name',
                  'village__name',
                  'rating']


class HotelFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Hotel
        fields = ['country__name',
                  'state__name',
                  'region__name',
                  'county__name',
                  'city__name',
                  'town__name',
                  'village__name',
                  'rating']


class RestaurantFilter(filters.FilterSet):
    rating__gte = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Restaurant
        fields = ['country__name',
                  'state__name',
                  'region__name',
                  'county__name',
                  'city__name',
                  'town__name',
                  'village__name',
                  'rating']


@method_decorator(cache_page(86400), name='home_cache')
class Home(ListView):
    model = Country
    template_name = 'google_trip/index.html'
    context_object_name = 'countries'
    ordering = 'name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all().order_by(
            '-number_of_review')[:3]
        context['tourist_attractions'] = TouristAttraction.objects.all().order_by(
            '-number_of_review')[:3]
        context['restaurants'] = Restaurant.objects.all().order_by(
            '-number_of_review')[:3]
        return context


class Geo(ListView):
    model = Country
    template_name = 'google_trip/geo.html'
    context_object_name = 'countries'


@method_decorator(cache_page(86400), name='tourist_attractions_cache')
class TouristAttractions(ListView):
    model = TouristAttraction
    context_object_name = 'tourist_attractions'
    paginate_by = 10
    ordering = '-number_of_review'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('name')
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.GET.get('country__name')
        if country is None:
            return qs
        return qs.filter(country__name=country)


@method_decorator(cache_page(86400), name='restaurants_cache')
class Restaurants(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    paginate_by = 10
    ordering = '-number_of_review'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('name')
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.GET.get('country__name')
        if country is None:
            return qs
        return qs.filter(country__name=country)


@method_decorator(cache_page(86400), name='hotels_cache')
class Hotels(ListView):
    model = Hotel
    context_object_name = 'hotels'
    paginate_by = 10
    ordering = '-number_of_review'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('name')
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


class APIRestaurantsList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().order_by('-number_of_review')
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter


class APIHotelsList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all().order_by('-number_of_review')
    serializer_class = HotelSerializer
    filterset_class = HotelFilter
