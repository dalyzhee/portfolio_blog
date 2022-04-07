from asyncio.windows_events import NULL
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, default='levis')
    body = models.TextField()
    image = models.ImageField(upload_to="blog", default=NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, default='tech')


    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.CharField(max_length=100, default='admin')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author