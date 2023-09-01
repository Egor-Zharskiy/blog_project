from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts_images")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    by_user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
