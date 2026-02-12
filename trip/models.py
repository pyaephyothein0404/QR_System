from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    number = models.CharField(max_length=100, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    qr_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.number
    

class Receipt(models.Model):
    number = models.CharField(max_length=100)
    qr_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='receipts/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number