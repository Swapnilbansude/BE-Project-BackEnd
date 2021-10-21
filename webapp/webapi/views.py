from django.shortcuts import render
from . models import User,CropDetails,AdvertisementDetails,ComplaintDetails,FarmersRequest,CustomersRequest
from rest_framework.permissions import IsAuthenticated
from . serializers import UserSerializer,CropDetailsSerializer,AdsDetailsSerializer,ComplaintDetailsSerializer,FarmersRequestSerializer,CustomersRequestSerializer
from rest_framework.generics import (ListCreateAPIView)
from rest_framework import generics 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CropDetailsList(generics.ListCreateAPIView):
    queryset = CropDetails.objects.all()
    serializer_class = CropDetailsSerializer
    permission_classes = [IsAuthenticated]

#display crop details by id
class CropDetailsById(generics.RetrieveUpdateDestroyAPIView):
    queryset = CropDetails.objects.all()
    serializer_class = CropDetailsSerializer
    permission_classes = [IsAuthenticated]

class AdsDetailsList(generics.ListCreateAPIView):
    queryset = AdvertisementDetails.objects.all()
    serializer_class = AdsDetailsSerializer
    permission_classes = [IsAuthenticated]

#get advertisement details by id
class AdsDetailsById(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvertisementDetails.objects.all()
    serializer_class = AdsDetailsSerializer
    permission_classes = [IsAuthenticated]

class ComplaintDetailsList(generics.ListCreateAPIView):
    queryset = ComplaintDetails.objects.all()
    serializer_class = ComplaintDetailsSerializer
    permission_classes = [IsAuthenticated]

class FarmersRequestList(generics.ListCreateAPIView):
    queryset = FarmersRequest.objects.all()
    serializer_class = FarmersRequestSerializer
    permission_classes = [IsAuthenticated]

class CustomersRequestList(generics.ListCreateAPIView):
    queryset = CustomersRequest.objects.all()
    serializer_class = CustomersRequestSerializer
    permission_classes = [IsAuthenticated]
