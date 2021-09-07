from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'barcode')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch_name', 'location')

class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'stores', 'supply_date')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'stores', 'sale_date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Sale, SaleAdmin)
