from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True) # Ensure unique category names
  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products_category')
  subcategory = models.CharField(max_length=200,null=True)
  quantity = models.IntegerField(default=0)
  image = models.ImageField(upload_to='product_images/', blank=True, null=True)

  def __str__(self):
    return self.name
