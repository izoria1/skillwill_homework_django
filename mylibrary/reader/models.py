from django.db import models
from django.contrib.auth.models import User
from book.models import Book  

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
