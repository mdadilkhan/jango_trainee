from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False) 
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=15)  
    password = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
