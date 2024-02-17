from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books')
    pages = models.IntegerField()
    count = models.IntegerField()


    def __str__(self):
        return self.title
    def is_avail(self):
        if self.count > 0:
            return True
        else:
            return False