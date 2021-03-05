from django.db import models

from mainapp.models.user import User


# Create your models here.
class BatchRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=20)
    data = models.JSONField()
    target_email = models.CharField(max_length=255)
    state = models.CharField(max_length=32)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
