from acess_the_Cam.views import upload_video
from acess_the_Cam.views import live_stream,status_view,list_videos
from django.urls import path,include
from django.shortcuts import render
urlpatterns = [
    path('u', upload_video, name='upload_video'),
    path('', live_stream, name='live_stream'),
    path('status', list_videos.as_view(), name='live_stream'),  # New URL
]
