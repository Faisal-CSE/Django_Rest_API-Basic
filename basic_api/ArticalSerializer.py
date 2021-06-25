from django.db.models import fields
from rest_framework import serializers
from .models import Artical


'''
    Model Serializer Format
'''
class ArticalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artical
        #fields = '__all__'
        fields = ['id', 'title', 'author', 'email', 'description', 'date']
        #fields = ['title', 'author', 'email', 'description', 'date']


'''
    Serializer Format
'''
#class ArticalSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=80)
    # author = serializers.CharField(max_length=120)
    # email = serializers.EmailField(max_length=100)
    # description = serializers.TextField()
    # date = serializers.DateTimeField()


    # def create(self, validate_data):
    #     return Artical.objects.create(validate_data)

    # def update(self, instance, validate_data):
    #     instance.title = validate_data.get('title', instance.title)
    #     instance.author = validate_data.get('author', instance.author)
    #     instance.email = validate_data.get('email', instance.email)
    #     instance.description = validate_data.get('description', instance.description)
    #     instance.date = validate_data.get('date', instance.date)

    #     instance.save()
    #     return instance