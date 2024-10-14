from django.contrib import admin
from django.urls import path,include
from add_aboutyou.views import about_you_data
urlpatterns = [
    path('', about_you_data.as_view(),name="about_you"),
]