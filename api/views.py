from rest_framework.views import APIView
#response will be given from Response function
from rest_framework.response import Response
from rest_framework import viewsets
from api import serializers
from api.models import UserProfile  

# Create your views here.
class SampleApiView(APIView):
    """The get method is responsible for handling the get requests"""
    def get(self,request,format=None):
        #always resposne should be in the form of dictionary
        return Response({'name':"SampleAPIView",'message':"Hello world"})


class UserProfileModelViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=UserProfile.objects.all() 