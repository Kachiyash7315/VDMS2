from django.db import models
from django.contrib.auth.models import User


# Create your models here.c

class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20, null=True)
    mobile = models.CharField(primary_key=True, max_length=20, blank=True)
    otp = models.CharField(max_length=6)

    # def __str__(self):
    #     return self.mobile


# class UserStudent(models.Model):
#     name = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField(max_length=20, null=True, blank=True)
#     mobile = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     # city = models.CharField(max_length=20, null=True, blank=True)
#     # state = models.CharField(max_length=20, null=True, blank=True)
#     # pin = models.IntegerField(max_length=20, null=True, blank=True)
#     # designation = models.CharField(max_length=20, null=True, blank=True)
