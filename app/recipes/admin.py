import recipes.models
import django.contrib.admin

django.contrib.admin.site.register(recipes.models.Recipe)

class IngredientAdmin(django.contrib.admin.ModelAdmin):
    fields = ['quantity', 'unit', 'item']

django.contrib.admin.site.register(recipes.models.Ingredient, IngredientAdmin)

django.contrib.admin.site.register(recipes.models.Review)
