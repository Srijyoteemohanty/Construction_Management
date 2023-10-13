from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    start_date = models.DateField()
    target_date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name
