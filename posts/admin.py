from django.contrib import admin
from posts.models import Post, Category
from users.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(User)
