from django.db import models


class Doctor(models.Model):
    """
    Doctor model for storing doctor information.
    """
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
    class Meta:
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['name']