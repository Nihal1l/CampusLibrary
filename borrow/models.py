from django.db import models
from django.core.validators import MinValueValidator
from book.models import Book
from uuid import uuid4
# Create your models here.

class BorrowRecord(models.Model):
    STATUS_CHOICES = [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
    ]

    # ✅ use string reference to avoid circular import
   
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, related_name="borrow_records")

    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Borrowed')

    def __str__(self):
        return f"{self.member.name} - ({self.status})"
    

    
class BorrowItem(models.Model):
    borrow = models.ForeignKey(
        BorrowRecord, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['borrow', 'book']]

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"    
