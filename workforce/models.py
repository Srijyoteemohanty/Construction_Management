from django.db import models

class workforce(models.Model):
    EMPLOYEE_CHOICES = (
        ('Skilled', 'Skilled'),
        ('Non-Skilled', 'Non-Skilled'),
    )

    emp_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    dob = models.DateField()
    adhar_card_no = models.CharField(max_length=12, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    skilled_or_non_skilled = models.CharField(max_length=15, choices=EMPLOYEE_CHOICES)




