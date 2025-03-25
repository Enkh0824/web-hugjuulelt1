from django.db import models

# Create your models here.
class Center(models.Model):
    code=models.CharField(max_length=2)
    city= models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city}. ({self.code})"

class Transport(models.Model):
    origin=models.ForeignKey(Center, on_delete=models.CASCADE, related_name="origin_city")
    destination= models.ForeignKey(Center, on_delete=models.CASCADE, related_name="dest_city")
    distance= models.IntegerField()
    def __str__(self):
        return f"{self.id}. {self.origin} -c {self.destination}"