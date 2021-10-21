from django.contrib import admin
from . models import User,CropDetails,AdvertisementDetails,ComplaintDetails,FarmersRequest,CustomersRequest
# Register your models here.

admin.site.register(User)
admin.site.register(CropDetails)
admin.site.register(AdvertisementDetails)
admin.site.register(ComplaintDetails)
admin.site.register(FarmersRequest)
admin.site.register(CustomersRequest)

