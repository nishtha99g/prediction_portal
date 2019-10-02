from django.db import models
from enumerations.enum import BloodGroup, Gender, Category
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, null=False ,default='')
    date_of_birth = models.DateField(default=date.today)
    gender = models.CharField(max_length=3, choices=[(tag.name, tag.value) for tag in Gender], default='')
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='profile_photo', help_text='Your Photo name should be same as your name',
                              blank=True, null=True)
    category = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in Category],
                                default='')
    blood_group = models.CharField(max_length=5, choices=[(tag.name, tag.value) for tag in BloodGroup],
                                   blank=True, null=True)
    verified = models.BooleanField(default=False)
    branch = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=True, default=0.0)
    projects=models.PositiveIntegerField(null=True, blank=True)
    description=models.CharField(max_length=500)
    Languages=models.CharField(max_length=150, null=True, blank=True)
    co_cur=models.BooleanField(default=False)

    class Meta:
        permissions = (
        )

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


    # Automatically Called Whenever an user instance is created
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
           user_profile = Profile.objects.create(user=user)
           user_profile.save()


    post_save.connect(create_profile, sender=User)




