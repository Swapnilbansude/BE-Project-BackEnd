from rest_framework.response import Response
from rest_framework import status
from . models import User,CropDetails,AdvertisementDetails
from rest_framework.permissions import IsAuthenticated
from . serializers import UserSerializer,CropDetailsSerializer
from rest_framework.decorators import api_view,permission_classes
from django.db import connection

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_ads_bycustomer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select * from webapi_advertisementdetails where phone = {phone}')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'id':result[0],
            'customer_name':result[1],
            'phone':result[2],
            'address':result[3],
            'crop_req':result[4],
            'quantity_req':result[5],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)