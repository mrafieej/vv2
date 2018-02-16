from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', default=None)
    email = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length=100, default=None)
    firstname = models.CharField(max_length=100, default=None)
    lastname = models.CharField(max_length=100, default=None)
    location = models.CharField(max_length=100, default=None)
    occupation = models.CharField(max_length=100, default=None)
    about = models.TextField(max_length=1000, default=None)
    profile_pic = models.ImageField(upload_to='media/profile_pics/', default=None)
    points = models.IntegerField(default=None)
    last_logged = models.DateTimeField(default=None)
    joined = models.DateTimeField(default=None)

    def __str__(self):
        return self.firstname + " " + self.lastname + " (" + self.email + ")"
