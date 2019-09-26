from django.urls import path, re_path
from . import views

app_name='student'

urlpatterns = [
path('register/', views.register, name='register'),
path('dashboard/', views.dashboard, name='dashboard'),
path('profile/', views.view_profile, name='view_profile'),
path('profile/update/', views.update_profile, name='update_profile'),
path('predict/',views.predict_data, name='predict_data'),
path('job/',views.pre_form, name='pre_form'),
]