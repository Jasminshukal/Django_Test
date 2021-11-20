from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=264,unique=True)

class Userdetail(models.Model):
    address=models.CharField(max_length=128)
    ph_no=models.CharField(max_length=128)
    user = models.OneToOneField(User, 
          on_delete = models.CASCADE, primary_key = True)
          