from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='created_products', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


