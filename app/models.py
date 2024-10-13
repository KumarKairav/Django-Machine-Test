from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name
