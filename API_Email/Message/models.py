from django.conf import settings
from django.db import models

# Create your models here.


class Message(models.Model):
    sender = models.EmailField(
        default=settings.EMAIL_HOST_USER, max_length=254, null=True, blank=True
    )
    receiver = models.TextField()
    subject = models.CharField(default="", max_length=100)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
