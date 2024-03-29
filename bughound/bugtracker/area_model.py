from django.db import models

from .program_model import Program


class Area(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, default='DEFAULT')

    def __str__(self):
        return self.name
