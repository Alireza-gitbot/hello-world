from django.contrib import admin
from django.contrib.admin import TabularInline

from basket.models import Basket, BasketLine


# Register your models here.

class BasketLineInline(admin.TabularInline):
    model = BasketLine


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']
    inlines = (BasketLineInline, )


admin.site.register(Basket, BasketAdmin)
