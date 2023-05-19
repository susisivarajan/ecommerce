from django.db import models

# Create your models here.
class ecommerce(models.Model):
    name=models.CharField(max_length=150)
    price=models.IntegerField()
    brand=models.TextField()
    size=models.TextField()
    details=models.TextField()
    image=models.ImageField(upload_to="image")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='ecommerce'
