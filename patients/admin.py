from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'created_by', 'created_at')
    list_filter = ('gender', 'created_at', 'created_by')
    search_fields = ('name', 'created_by__name', 'created_by__email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)