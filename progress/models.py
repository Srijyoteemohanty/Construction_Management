from django.db import models
from sites.models import Site  # Import the Site model

class progress(models.Model):
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField()
    units_completed = models.DecimalField(max_digits=10, decimal_places=2)

