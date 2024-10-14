from django.shortcuts import render
from add_project.models import create_project
from add_project.serializers import Create_project_serializers
from rest_framework import generics
class update_project(generics.RetrieveUpdateAPIView):
    queryset=create_project.objects.all()
    serializer_class=Create_project_serializers
