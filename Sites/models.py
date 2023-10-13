from django.db import models

class Site(models.Model):
    site_name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    total_work = models.DecimalField(max_digits=10, decimal_places=2)
    UNIT_CHOICES = (
        ('KM', 'Kilometers'),
        ('M', 'Meters'),
        ('MI', 'Miles'),
    )
    unit_of_work = models.CharField(max_length=2, choices=UNIT_CHOICES)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    #project = models.ForeignKey('projects', on_delete=models.CASCADE)  # Reference to the Project model

    def __str__(self):
        return self.site_name
