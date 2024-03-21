from django.contrib import admin
from .models import Vehicle, VehicleBrand, VehicleModel, VehicleColor, VehicleCondition

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'color', 'purchase_year', 'condition')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(VehicleColor)
admin.site.register(VehicleCondition)