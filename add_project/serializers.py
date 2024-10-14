from rest_framework import serializers
from add_project.models import create_project
class Create_project_serializers(serializers.ModelSerializer):
    class Meta:
        model= create_project
        fields="__all__"
