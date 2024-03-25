from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to="images")

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return f"{self.title}"
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-author"]

    def __str__(self):
        return f"{self.author}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
