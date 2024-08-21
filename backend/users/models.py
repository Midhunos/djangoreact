from django.contrib.auth.models import User
from django.db import models

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_of', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} is friends with {self.friend.username}"
