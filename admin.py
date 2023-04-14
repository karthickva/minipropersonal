from django.contrib import admin
from personal_app.models import Personal_information

class Peradmin(admin.ModelAdmin):
    perdetails=["Name"," Father_Name","Mother_Name","DateOfBirth","Gender","Native_District","Martial_status","Language_known"," Higher_Qualification","Project","Permanaent_address","phone_number","EmailID"]

admin.site.register(Personal_information,Peradmin)

