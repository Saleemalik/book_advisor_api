from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from api.models import Advisor

from api.serializers import AdvisorSerializer
from rest_framework.views import APIView


# Create your views here.



class AddAdivisor(APIView):
    serializer_class = AdvisorSerializer

    def post(self, request, formate = None):
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status =status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
