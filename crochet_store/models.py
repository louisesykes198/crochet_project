from django.db import models

class CrochetItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='crochet_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        app_label = 'crochet_store'
    
    def __str__(self):
        return self.name

