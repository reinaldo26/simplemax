from django.contrib import admin
from . import models

class ItemOrderInLine(admin.TabularInline):
    model = models.ItemOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderInLine]


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.ItemOrder)
