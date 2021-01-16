from django.contrib import admin
from .models import Office, Services, Employee


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['office', 'active', 'modified']


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'icon', 'active', 'modified']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'office','active', 'modified']