from django.db import models

# Create your models here.
class myAdminPanel(models.Model):
    image = models.TextField(max_length=100,null=False)
    title = models.CharField(max_length=100,null=False)
    description = models.TextField(max_length=500,null=False)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField()
    slugTitle = models.SlugField(max_length=100)
    isActive = models.BooleanField(default=False)
    

