from django.contrib import admin

# Register your models here.
from .models import *

class ModeloAdmin(admin.ModelAdmin):
	list_display = ["name", "stock", "price"]

class OrderDisplay(admin.ModelAdmin):
	list_display = [ 'date', 'full_name', 'id', 'product_n']

admin.site.register(Bikes, ModeloAdmin)
admin.site.register(Books, ModeloAdmin)
admin.site.register(CD, ModeloAdmin)
admin.site.register(Product, ModeloAdmin)
admin.site.register(BuyOrders, OrderDisplay)
