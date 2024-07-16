from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    persons_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')
    description = models.CharField(max_length=256, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_percent = models.IntegerField(default=0, help_text="Процент скидки для блюда")
    def __str__(self):
        return self.name
    
    def price_after_discount(self):
        if self.discount_percent > 0:
            discount_price = self.price - (self.price * self.discount_percent / 100)
            return discount_price
        return self.price
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.total_price = self.dish.price * self.quantity
        super().save(*args, **kwargs)