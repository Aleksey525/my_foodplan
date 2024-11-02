from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Recipes, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview', 'publication')
    search_fields = ('title',)
    list_filter = ('ingredients',)
    fields = ('title', 'description', 'image', 'image_preview', 'publication')
    readonly_fields = ('image_preview',)
    inlines = [
        RecipeIngredientInline
    ]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />')
        return "Нет изображения"

    image_preview.allow_tags = True
    image_preview.short_description = 'Предпросмотр изображения'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title',)



