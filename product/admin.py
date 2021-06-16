from django.contrib import admin
from . import models
from .models import Product, Variation

class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_short', 'get_format_price', 'get_format_price_promo']
    inlines = [VariationInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
