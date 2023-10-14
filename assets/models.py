from django.db import models

class assets(models.Model):
    ASSET_CATEGORY_CHOICES = (
        ('Movable', 'Movable'),
        ('Immovable', 'Immovable'),
    )

    OWNERSHIP_CHOICES = (
        ('Owned', 'Owned'),
        ('Rented', 'Rented'),
    )

    asset_name = models.CharField(max_length=255)
    category = models.CharField(max_length=15, choices=ASSET_CATEGORY_CHOICES)
    ownership = models.CharField(max_length=15, choices=OWNERSHIP_CHOICES)

