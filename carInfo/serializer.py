from django.db.models import fields
from rest_framework import serializers
from .models import CarSpaces

class CarSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpaces
        fields = ['id', 'car_plan', 'car_plan', 'car_brand', 'car_model', 'production_year', 'car_body', 'engine_type']