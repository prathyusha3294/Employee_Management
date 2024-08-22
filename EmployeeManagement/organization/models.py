from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20)
    addressDetails = models.JSONField(blank=True,null=True)
    workExperience = models.JSONField(blank=True,null=True)  # For Work Experience list of dictionaries
    qualifications = models.JSONField(blank=True,null=True)  # For Qualifications list of dictionaries
    projects = models.JSONField(blank=True,null=True)  # For Projects list of dictionaries
    # photo = models.TextField(blank=True, null=True)  # Store base64 image data

    def __str__(self):  
        return self.name
