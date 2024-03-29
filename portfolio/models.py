from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, default="first")
    description = models.TextField()
    technology = models.CharField(max_length=200, default="python")
    image = models.ImageField(upload_to="images")


    def __str__(self):
        return self.title
