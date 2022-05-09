from django.db import models

# Create your models here.
class Organization(models.Model):
    org_id = models.AutoField(primary_key=True, unique=True)
    org_name = models.CharField(max_length=25)
    org_email = models.EmailField(unique=True)
    org_pw = models.TextField(max_length=100)
    org_status = models.CharField(max_length=8)