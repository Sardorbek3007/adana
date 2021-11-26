from django.db import models

# Create your models here.
class Menyu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    content = models.TextField(default=0)
    video = models.CharField(max_length=300)
    category = models.ForeignKey('Category', related_name="menyu", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Connection(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)