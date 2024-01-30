from django.db import models

# Create your models here.


class StudentModel(models.Model):
    Name = models.CharField(max_length=100, default = None)
    Email_Id = models.CharField(max_length=100)
    Phone_No =  models.BigIntegerField()
    UserName = models.CharField(max_length=100 ,  unique=True)
    Password=  models.CharField(max_length=100)


class LoginUser(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    