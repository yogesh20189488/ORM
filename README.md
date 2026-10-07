# Ex02 Django ORM Web Application
## Date: 07/10/2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
model.py
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

admin.py
from django.contrib import admin
from .models import Vehicle_Details_DB,Vehicle_Details_DBAdmin
admin.site.register(Vehicle_Details_DB,Vehicle_Details_DBAdmin)


```

## OUTPUT

![alt text](<Screenshot (11).png>)

## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
