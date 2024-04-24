from django.db import models

class Book(models.Model):
    idbook = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    describe = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
