from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email', 'created_at')
    list_filter = ('specialization', 'created_at')
    search_fields = ('name', 'specialization', 'email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)