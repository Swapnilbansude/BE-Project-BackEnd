from rest_framework.response import Response
from rest_framework import status
from . models import FarmersRequest
from rest_framework.permissions import IsAuthenticated
from . serializers import FarmersRequestSerializer
from rest_framework.decorators import api_view,permission_classes
from django.db import connection

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def frequest_by_farmer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select cname,cphone,cadd,crop_req,quantity_req,status from webapi_farmersrequest where fphone = {phone}')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'cname':result[0],
            'cphone':result[1],
            'cadd':result[2],
            'crop_req':result[3],
            'quantity_req':result[4],
            'status':result[5],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def frequest_to_customer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select * from webapi_farmersrequest where cphone = {phone} and status = "Pending"')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'id':result[0],
            'fname':result[1],
            'fphone':result[2],
            'fadd':result[3],
            'cname':result[4],
            'cphone':result[5],
            'cadd':result[6],
            'crop_req':result[7],
            'quantity_req':result[8],
            'status':result[9],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cust_response_accept(request,id):
    cursor=connection.cursor()
    cursor.execute(f' update webapi_farmersrequest set status = "Accepted" where id = {id}')
    
    payload = {"message" : "request accepted "}

    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cust_response_reject(request,id):
    cursor=connection.cursor()
    cursor.execute(f' update webapi_farmersrequest set status = "Rejected" where id = {id}')
    
    payload = {"message" : "request accepted "}

    return Response(data=payload, status=status.HTTP_200_OK)
