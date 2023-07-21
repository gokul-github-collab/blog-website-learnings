from typing import Any
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excert = models.CharField(max_length=300)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=1000)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
