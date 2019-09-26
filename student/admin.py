from django.contrib import admin
from .models import Profile, Training_Prediction

class ProfileDisplay(admin.ModelAdmin):
    list_display= ['user', 'roll_no']
    
admin.site.register(Profile, ProfileDisplay)

class DataDisplay(admin.ModelAdmin):
    list_display= ['roll_no','cgpa']

admin.site.register(Training_Prediction, DataDisplay)