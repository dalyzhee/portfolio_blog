from django.contrib import admin
from .models import Comment, Post, Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)