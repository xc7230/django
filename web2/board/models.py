from django.db import models
from django.contrib.auth.models import User
class Board(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
# Create your models here.
