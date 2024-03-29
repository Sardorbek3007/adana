from rest_framework import serializers
from .models import *


class MenyuSerializer(serializers.ModelSerializer):    
    class Meta():

        model = Menyu
        fields = '__all__'

    def to_representation(self, instance):        
        data = super().to_representation(instance)
        categories = {}
        for category in Category.objects.all().values():
            categories[category["id"]] = category["name"]            
                
        data["category"]=categories[data["category"]]
        return data

class CategorySerializer(serializers.ModelSerializer):
    menyu = MenyuSerializer(read_only=True, many=True)

    class Meta():
        model = Category
        fields = '__all__'


class SpecialSerializer(serializers.ModelSerializer):
    class Meta():
        model = Special
        fields = '__all__'


    def to_representation(self, instance):        
        data = super().to_representation(instance)
        categories = {}
        for category in Category_1.objects.all().values():
            categories[category["id"]] = category["name"]            
                
        data["category"]=categories[data["category"]]
        return data

class Category_1Serializer(serializers.ModelSerializer):
    special = SpecialSerializer(read_only=True, many=True)
    class Meta():
        model = Category_1
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    class Meta():
        model = Picture
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Video
        fields = '__all__'

class ChefSerializer(serializers.ModelSerializer):
    class Meta():
        model = Chef
        fields = '__all__'


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Connection
        fields = '__all__'

class CardItemSerializer(serializers.ModelSerializer):    

    class Meta():
        model = CardItem
        fields = '__all__'
 
class CardSerializer(serializers.ModelSerializer):    
    carditems = CardItemSerializer(read_only=True, many=True)
    class Meta():
        model = Card
        fields = '__all__'