from django.contrib import admin
from .models import Profile

class ProfileDisplay(admin.ModelAdmin):
    list_display= ['user', 'roll_no']
    
admin.site.register(Profile, ProfileDisplay)