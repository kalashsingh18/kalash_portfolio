from add_project.serializers import Create_project_serializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny 
from rest_framework import generics
from add_project.models import create_project
@api_view(["POST"])
@permission_classes([AllowAny])
def add_project(request):
    serializer = Create_project_serializers(data=request.data,many=True)  # Use `data=request.data` for POST data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@permission_classes([AllowAny])
class listallproject(generics.ListCreateAPIView):
    queryset = create_project.objects.all()
    serializer_class = Create_project_serializers
