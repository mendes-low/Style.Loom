from django.contrib import admin
from .models import Clothes

admin.site.register(Clothes)


# class ClothesAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'image']
