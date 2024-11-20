from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=11)
    weight = models.IntegerField(default=0)



#run migrations
#python3  manage.py makemigrations
#python3 manage.py migrate


    
