from django.db import models

# Create your models here.
class Flowers(models.Model):
    name=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    img=models.ImageField(upload_to='gallery',null=True)

    def __str__(self):
        return self.name
