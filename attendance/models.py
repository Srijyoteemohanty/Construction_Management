from django.db import models
from workforce.models import workforce  # Import the Workforce model

class attendance(models.Model):
    emp_id = models.ForeignKey(workforce, on_delete=models.CASCADE)
    date = models.DateField()

