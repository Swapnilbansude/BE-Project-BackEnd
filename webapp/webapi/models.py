from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, AbstractUser
)

# Create your models here.

''' For Storing Basic User Information ''' 

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,unique=True,blank=False)
    email = models.EmailField(max_length=255)
    aadhar_no = models.CharField(max_length=255,default=None)
    address = models.TextField(blank=False)
    category = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['first_name','last_name','username',
                        'aadhar_no','address','email','is_admin','category','password']

    USERNAME_FIELD = 'phone'


    def get_username(self):
        return self.phone

class CropDetails(models.Model):
    farmer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    crop_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def get_username(self):
        return self.farmer_name

class AdvertisementDetails(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    crop_req = models.CharField(max_length=255)
    quantity_req = models.IntegerField()

    def get_username(self):
        return self.customer_name

class ComplaintDetails(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    complaint_type = models.CharField(max_length=255)
    description = models.TextField()

    def get_username(self):
        return self.name

class FarmersRequest(models.Model):
    fname = models.CharField(max_length=255)
    fphone = models.CharField(max_length=255)
    fadd = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    cphone = models.CharField(max_length=255)
    cadd = models.CharField(max_length=255)
    crop_req = models.CharField(max_length=255)
    quantity_req = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def get_username(self):
        return self.fname

class CustomersRequest(models.Model):
    cname = models.CharField(max_length=255)
    cphone = models.CharField(max_length=255)
    cadd = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    fphone = models.CharField(max_length=255)
    fadd = models.CharField(max_length=255)
    crop = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def get_username(self):
        return self.fname
