from django.db import models
from userprofiles.models import UserProfile
import uuid


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80, default=None)
    location = models.CharField(max_length=30, default=None)
    description = models.TextField(default=None)
    bedrooms = models.IntegerField(default=None)
    bathrooms = models.FloatField(default=None)
    capacity = models.IntegerField(default=None)
    square_footage = models.IntegerField(default=None)
    street = models.CharField(max_length=120, default=None)
    city = models.CharField(max_length=80, default=None)
    zip_code = models.IntegerField(default=None)
    cats_ok = models.BooleanField(default=None)
    dogs_ok = models.BooleanField(default=None)
    smoking_ok = models.BooleanField(default=None)
    availability_from = models.DateField(default=None)
    availability_to = models.DateField(default=None)
    points_per_night = models.IntegerField(default=None)
    deposit = models.IntegerField(default=None)
    image_1 = models.ImageField(upload_to='media/listings/', default=None)
    image_2 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_3 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_4 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_5 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_6 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_7 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_8 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_9 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    image_10 = models.ImageField(upload_to='media/listings/', default=None, blank=True)
    pub_date = models.DateTimeField(default=None)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def formatDate(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.description[:100]
