from django.urls import path, include
from webapi import views 
from . views import UserList,CropDetailsList,AdsDetailsList,ComplaintDetailsList,CropDetailsById,AdsDetailsById,FarmersRequestList,CustomersRequestList
from .crop_views import display_crop_byfarmer
from .ads_views import display_ads_bycustomer
from .frequest_views import frequest_by_farmer,frequest_to_customer,cust_response_accept,cust_response_reject
from .crequest_views import crequest_by_customer,crequest_to_farmer,farm_response_accept,farm_response_reject

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('allusers/', UserList.as_view()),
    #All crop details
    path('cropdetails/', CropDetailsList.as_view()),
    
    #All Advertisement Details
    path('adsdetails/', AdsDetailsList.as_view()),

    #Post Complaints
    path('complaints/', ComplaintDetailsList.as_view()),
    
    #Particular Customer Advertisements Details
    path('customeradspdetails/<str:phone>', display_ads_bycustomer),
    path('adsbyid/<int:pk>', AdsDetailsById.as_view()),

    #Send Farmer Request to the customer(Post details)
    path('frequest/',FarmersRequestList.as_view()),

    #Get Particular farmers all requests
    path('frequest/<str:phone>', frequest_by_farmer),

    #Get all request send to particular customer
    path('frequesttocustomer/<str:phone>', frequest_to_customer),

    #Send accept response to farmers request by id
    path('cresponse/accept/<int:id>', cust_response_accept),
    path('cresponse/reject/<int:id>', cust_response_reject),

    #Send Customer Request to the customer(Post details)
    path('crequest/',CustomersRequestList.as_view()),

    #Get Particular customers all requests
    path('crequest/<str:phone>', crequest_by_customer),

    #Get all request send to particular farmer
    path('crequesttofarmer/<str:phone>', crequest_to_farmer),

    #Send accept response to customers request by id
    path('fresponse/accept/<int:id>', farm_response_accept),
    path('fresponse/reject/<int:id>', farm_response_reject),

    #Particular Farmer Crop Details
    path('farmercropdetails/<str:phone>', display_crop_byfarmer),
    path('cropbyid/<int:pk>', CropDetailsById.as_view())
]