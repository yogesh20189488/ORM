from django.db import models
from django.contrib import admin
class Vehicle_Details_DB(models.Model):
    customer_name=models.CharField(max_length=10)
    vehicl_model=models.CharField(max_length=20)
    vehicl_model_num=models.IntegerField()
    phone_number_1=models.IntegerField()
    phone_number_2=models.CharField(max_length=20)
    fuel_type=models.TextField()
    licence_num=models.CharField(max_length=10,primary_key=True)
    alternate_num=models.IntegerField()
class Vehicle_Details_DBAdmin(admin.ModelAdmin):
    licence_num=models.CharField(max_length=10,primary_key=True)
    licence_num=models.CharField(max_length=10,primary_key=True)
    list_display=["customer_name","vehicl_model","vehicl_model_num","phone_number_1","phone_number_2","fuel_type","licence_num","alternate_num"]
