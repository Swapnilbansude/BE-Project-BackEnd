from djoser.serializers import UserCreateSerializer
from .models import *
from rest_framework import serializers
from . models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','first_name','last_name','phone','username',
                        'aadhar_no','address','email','is_admin','category','password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','phone','username',
                        'aadhar_no','address','email','is_admin','category','password')

class CropDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropDetails
        fields = '__all__'

class AdsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementDetails
        fields = '__all__'

class ComplaintDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintDetails
        fields = '__all__'

class FarmersRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersRequest
        fields = '__all__'

class CustomersRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomersRequest
        fields = '__all__'