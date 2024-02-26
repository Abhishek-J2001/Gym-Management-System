from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

class ManagePackage(models.Model):
    categoryname = models.CharField(max_length=100, null=True, blank=True)
    packagename = models.CharField(max_length=100, null=True, blank=True)
    Packageimage = models.ImageField(upload_to="Profile", null=True, blank=True)

class AddPackage(models.Model):
    categoryname = models.CharField(max_length=100, null=True, blank=True)
    packagename = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    duraction = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

