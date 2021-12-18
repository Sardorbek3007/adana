from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Menyu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    content = models.TextField(default=0)
    category = models.ForeignKey('Category', related_name="menyu", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    def get_image(self):
        return self.image.url

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Special(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    content = models.TextField(default=0)
    category = models.ForeignKey('Category_1', related_name="special", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category_1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Picture(models.Model):
    image = models.ImageField()

class Video(models.Model):
    video = models.CharField(max_length=1000)

class Chef(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    content = models.TextField(default=0)
    telegram = models.CharField(max_length=100, default="")
    instagram = models.CharField(max_length=100, default="")
    facebook = models.CharField(max_length=100, default="")

class Connection(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

class Card(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)   
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}: {self.added_date}"

class CardItem(models.Model):
    product = models.ForeignKey(Menyu, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Card, related_name="carditems",on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.product.name