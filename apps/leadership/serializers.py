from rest_framework import serializers
from models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location

# class PoliticianSerializer(serializers.ModelSerializer):
#     location = LocationSerializer(many=True)
#     district = DistrictSerializer(many=False)
#     class Meta:
#         model = Politician
#
# class DistrictSerializer(serializers.ModelSerializer):
#     location = LocationSerializer(many=True)
#
#     class Meta:
#         model = District

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users