from django.contrib import admin
from .models import Office, Services, Employee, Features


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['office', 'active', 'modified']


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'active', 'modified']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'office','active', 'modified']


@admin.register(Features)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'modified']
