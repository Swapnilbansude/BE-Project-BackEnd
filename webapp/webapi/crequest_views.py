from rest_framework.response import Response
from rest_framework import status
from . models import CustomersRequest
from rest_framework.permissions import IsAuthenticated
from . serializers import CustomersRequestSerializer
from rest_framework.decorators import api_view,permission_classes
from django.db import connection

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crequest_by_customer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select fname,fphone,fadd,crop,quantity,status from webapi_customersrequest where cphone = {phone}')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'fname':result[0],
            'fphone':result[1],
            'fadd':result[2],
            'crop':result[3],
            'quantity':result[4],
            'status':result[5],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crequest_to_farmer(request,phone):
    cursor=connection.cursor()
    cursor.execute(f'select * from webapi_customersrequest where fphone = {phone} and status = "Pending"')
    row = cursor.fetchall()

    content = {}
    payload = []

    for result in row:
        content = {
            'id':result[0],
            'cname':result[1],
            'cphone':result[2],
            'cadd':result[3],
            'fname':result[4],
            'fphone':result[5],
            'fadd':result[6],
            'crop':result[7],
            'quantity':result[8],
            'status':result[9],
        }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def farm_response_accept(request,id):
    cursor=connection.cursor()
    cursor.execute(f' update webapi_customersrequest set status = "Accepted" where id = {id}')
    
    payload = {"message" : "request accepted "}

    return Response(data=payload, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def farm_response_reject(request,id):
    cursor=connection.cursor()
    cursor.execute(f' update webapi_customersrequest set status = "Rejected" where id = {id}')
    
    payload = {"message" : "request rejected "}

    return Response(data=payload, status=status.HTTP_200_OK)
