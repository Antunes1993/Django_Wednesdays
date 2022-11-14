from django.contrib import admin
from .models import Equipment 
from .models import Employee
from .models import Maintenance


# Register your models here.
admin.site.register(Employee)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('tag','address','type')
    ordering = ('tag',)
    search_fields = ('tag', 'address')


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_identification','maintenance_date','name')    
    list_filter = ('equipment','manager','maintenance_date')
    ordering = ('maintenance_date',)
    search_fields = ('manager', 'equipment')