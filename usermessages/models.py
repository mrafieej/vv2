from django.db import models
from userprofiles.models import UserProfile
from listing.models import Listing


class Message(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    sender = models.ForeignKey(UserProfile, related_name='sender_user_profile', on_delete=models.CASCADE, default=None)
    receiver = models.ForeignKey(UserProfile, related_name='receiver_user_profile', on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=2000, default=None)
    message_date = models.DateTimeField(default=None)
    is_read = models.BooleanField(default=None)

    def __str__(self):
        return self.body[:60]
