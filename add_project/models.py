from django.db import models

# Create your models here.
class create_project(models.Model):
    project_name=models.CharField(max_length=1234)
    project_discription=models.TextField(null=False,blank=False)
    git_hub_url=models.URLField()
    live_url=models.URLField()
    def __str__(self):
        return self.project_name