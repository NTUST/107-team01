from django.db import models
# Create your models here.
class restaurant(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField(blank= True)
    address = models.CharField(max_length=100,blank=True)
    price = models.CharField(max_length=100,blank=True)
    worktime = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='imageforrestaurant')

    def __str__(self):
        return self.name
