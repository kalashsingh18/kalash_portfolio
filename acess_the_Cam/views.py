from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import VideoSerializer
from django.views.decorators.csrf import csrf_exempt
from acess_the_Cam.models import Video
from rest_framework import generics
from django.shortcuts import render
@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])  # Allow any user to upload videos
def upload_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        print("here")
        serializer.save()
        return Response({'message': 'Video uploaded successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Upload failed', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

def live_stream(request):
    return render(request, 'live_stream.html')
from django.db import connections

@api_view(['GET'])
@permission_classes([AllowAny])  # Allows public access
def status_view(request):
    response_data = {
        "status": "ok",
        "service": "User Authentication Module",
        
    }
    
    # Optional: Check database connection
    try:
        db_conn = connections['default']
        db_conn.cursor()
        response_data['database'] = "connected"
    except Exception as e:
        response_data['database'] = f"error: {str(e)}"
        response_data['status'] = "error"
    
    return Response(response_data, status=200 if response_data["status"] == "ok" else 500)
@permission_classes([AllowAny])
class list_videos(generics.ListCreateAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
