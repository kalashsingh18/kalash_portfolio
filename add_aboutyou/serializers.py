from rest_framework import serializers
from add_aboutyou.models import about_you
class about_you_serializers(serializers.ModelSerializer):
    class Meta:
        model= about_you
        fields="__all__"
