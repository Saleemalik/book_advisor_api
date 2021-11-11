from django.shortcuts import render
from .serializers import *

from rest_framework.response import Response

from rest_framework import generics, permissions

# Create your views here.

# Register API
class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "messages": "Sent otp to the registered mobile number",
        "error": False,
        
        })
