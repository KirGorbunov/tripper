from django.urls import path
from .views import Home, TouristAttractions, Restaurants, Hotels, \
    ViewAttraction, ViewRestaurant, ViewHotel, Geo, \
    APITouristAttractionsList, APIRestaurantsList, APIHotelsList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tourist-attractions/', TouristAttractions.as_view(),
         name='tourist_attractions_list'),
    path('restaurants/', Restaurants.as_view(), name='restaurants_list'),
    path('hotels/', Hotels.as_view(), name='hotels_list'),
    path('tourist-attractions/<int:pk>/', ViewAttraction.as_view(),
         name='view_attraction'),
    path('restaurants/<int:pk>/', ViewRestaurant.as_view(),
         name='view_restaurant'),
    path('hotels/<int:pk>/', ViewHotel.as_view(), name='view_hotel'),
    path('geo/', Geo.as_view(), name='geo'),
    path('api/v1/tourist-attractions/', APITouristAttractionsList.as_view()),
    path('api/v1/restaurants/', APIRestaurantsList.as_view()),
    path('api/v1/hotels/', APIHotelsList.as_view()),
]
