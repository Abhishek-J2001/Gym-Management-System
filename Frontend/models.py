from django.db import models

# Create your models here.

class contact(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class payment(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    State = models.CharField(max_length=200, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    NameOnCard = models.CharField(max_length=200, null=True, blank=True)
    CardNumber = models.IntegerField(null=True, blank=True)
    ExpMonth = models.CharField(max_length=200, null=True, blank=True)
    ExpYear = models.IntegerField(null=True, blank=True)
    CVV = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

class blog(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class RegisterDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile", null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)