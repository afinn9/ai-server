from django.db import models


class BlacklistedToken(models.Model):
    token = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token


class User(models.Model):
    username = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.username
