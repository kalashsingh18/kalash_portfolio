from django.db import models
class about_you(models.Model):
    about_you_discription=models.TextField()
    urls=models.JSONField(default=dict)
# Create your models here.
