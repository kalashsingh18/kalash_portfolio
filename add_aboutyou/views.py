from django.shortcuts import render
from rest_framework import generics
from add_aboutyou.serializers import  about_you_serializers
from add_aboutyou.models import about_you
class about_you_data(generics.ListCreateAPIView):
    queryset=about_you.objects.all()
    serializer_class=about_you_serializers
# Create your views here.