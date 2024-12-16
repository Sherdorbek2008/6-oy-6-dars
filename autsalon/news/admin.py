from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Brand, Car

class CarInline(admin.TabularInline):
    model = Car
    extra = 1

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [CarInline]

class CarAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'year', 'price', 'brand']
    list_filter = ['brand']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
