from django.db import models
from workforce.models import workforce  # Import the Workforce model

class expense(models.Model):
    EXPENSE_CATEGORY_CHOICES = (
        ('Assets', 'Assets'),
        ('Consumable', 'Consumable'),
        ('Workforce Payment', 'Workforce Payment'),
    )

    category = models.CharField(max_length=20, choices=EXPENSE_CATEGORY_CHOICES)
    reference = models.ForeignKey(workforce, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

