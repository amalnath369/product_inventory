from django.db import models
from core.models import BaseModel
from django.core.validators import MinValueValidator



class Product(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    
    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"
    

    def decrease_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock. Available: {self.stock}")
        
        self.stock -= quantity
        self.save()
    

    def increase_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.stock += quantity
        self.save()