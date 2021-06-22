from django.db import models
from django.contrib.auth.models import User

class Glass(models.Model):
    Name = models.CharField(max_length=64)
    Discription = models.TextField()
    Admine = models.ForeignKey(User(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name