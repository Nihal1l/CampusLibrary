from django.db import models

from members.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    ISBN = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.title
"""
<Product: Laptop> id, name
product_id
product_name
"""