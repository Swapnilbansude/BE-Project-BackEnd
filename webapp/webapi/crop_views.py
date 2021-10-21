from rest_framework.response import Response
from rest_framework import status
from . models import User,CropDetails
from rest_framework.permissions import IsAuthenticated
from . serializers import UserSerializer,CropDetailsSerializer
from rest_framework.decorators import api_view,permission_classes
from django.db import connection

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_crop_byfarmer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select * from webapi_cropdetails where phone = {phone}')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'id':result[0],
            'farmer_name':result[1],
            'phone':result[2],
            'address':result[3],
            'crop_name':result[4],
            'quantity':result[5],
            'price':result[6],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

'''@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_crop_byid(request,id):
    cursor=connection.cursor()
    cursor.execute(f'select * from webapi_cropdetails where id = {id}')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'id':result[0],
            'farmer_name':result[1],
            'phone':result[2],
            'address':result[3],
            'crop_name':result[4],
            'quantity':result[5],
            'price':result[6],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)
    '''