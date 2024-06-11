from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name=models.TextField(max_length=122)
    
    def __str__(self) -> str:
        return f"{self.name}"
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,default='coding')

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
