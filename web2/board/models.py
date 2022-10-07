from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
# Create your models here.
