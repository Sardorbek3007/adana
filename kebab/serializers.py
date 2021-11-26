from rest_framework import serializers
from .models import *


class MenyuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menyu
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    menyu = MenyuSerializer(read_only=True, many=True)

    class Meta():
        model = Category
        fields = '__all__'




class ConnectionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Connection
        fields = '__all__'