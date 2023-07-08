from django.db import models
from django.contrib.auth.models import User
from management.models import BaseModel
# Create your models here.


# override the default user model
class Profile(BaseModel):
    """Profile model for users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.user.username
