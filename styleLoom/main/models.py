from django.db import models

class Clothes(models.Model):
    GENDER_CHOICES = [
        ("men", "Men"),
        ("women", "Women"),
        ("kid", "Kid"),
    ]

    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='clothes/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
