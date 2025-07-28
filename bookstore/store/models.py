from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('mystery', 'Mystery & Thriller'),
        ('nonfiction', 'Non-Fiction'),
        ('romance', 'Romance'),
        ('scifi', 'Sci‑Fi & Fantasy'),
        ('education', 'Educational & Academic'),
        ('children', 'Children & Young Adult'),
        ('tech', 'Tech & Programming'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
