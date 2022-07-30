from django.contrib import admin
from .models import Product



# ************** Register Models **************

# + models created for the product details
# + that the customers might see or query the system
# + are registered here


admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','id')
