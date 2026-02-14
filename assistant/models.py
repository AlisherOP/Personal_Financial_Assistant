from django.db import models
from django.contrib.auth.models import User
from .utils import extract_receipt_data
# Create your models here.
class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    receipt_image = models.ImageField(upload_to='receipts/')
    merchant = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            m, a = extract_receipt_data(self.receipt_image.path)
            self.merchant = m
            # Ensure 'a' is a valid number before saving
            try:
                self.amount = float(a)
            except (ValueError, TypeError):
                self.amount = 0.00
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.merchant or 'Processing...'} - {self.amount or '0.00'}"

