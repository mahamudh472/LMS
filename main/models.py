from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True)
    author = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    image = models.ImageField(upload_to='books', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True, default=1)


    def __str__(self):
        return self.title
    def is_avail(self):
        if self.count > 0:
            return True
        else:
            return False