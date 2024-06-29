from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class PurchaseHistory(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title