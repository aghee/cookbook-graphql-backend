from django.contrib import admin
from ingredients import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes', 'category')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)

admin.site.index_title = 'CookBook'
admin.site.site_title = 'CookBook'
admin.site.site_header = 'CookBook'