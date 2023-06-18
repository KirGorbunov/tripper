from rest_framework import serializers
from .models import TouristAttraction, Restaurant, Hotel


class TouristAttractionSerializer(serializers.ModelSerializer):
    x = serializers.DecimalField(source='rating', max_digits=4, decimal_places=3, coerce_to_string=False)
    y = serializers.IntegerField(source='number_of_review')
    country_name = serializers.CharField(source='country.name', allow_null=True)

    class Meta:
        model = TouristAttraction
        fields = ('id', 'country_id', 'country_name', 'name', 'x', 'y', 'photo', 'latitude', 'longitude')


class RestaurantSerializer(serializers.ModelSerializer):
    x = serializers.DecimalField(source='rating', max_digits=4, decimal_places=3, coerce_to_string=False)
    y = serializers.IntegerField(source='number_of_review')
    country_name = serializers.CharField(source='country.name', allow_null=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'country_id', 'country_name', 'name', 'x', 'y', 'photo', 'latitude', 'longitude')


class HotelSerializer(serializers.ModelSerializer):
    x = serializers.DecimalField(source='rating', max_digits=4, decimal_places=3, coerce_to_string=False)
    y = serializers.IntegerField(source='number_of_review')
    country_name = serializers.CharField(source='country.name', allow_null=True)

    class Meta:
        model = Hotel
        fields = ('id', 'country_id', 'country_name', 'name', 'x', 'y', 'photo', 'latitude', 'longitude')