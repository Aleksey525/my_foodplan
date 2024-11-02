from django.db import models


class Recipes(models.Model):
    PUBLICATION_CHOICES = (
            ('Published', 'Опубликовано'),
            ('archived', 'В архиве'),
        )
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    description = models.TextField(blank=True, verbose_name="Описание рецепта")
    ingredients = models.ManyToManyField('Ingredient', verbose_name="Ингредиенты")
    image = models.ImageField(upload_to='media/recipes/img', verbose_name="Картинка с рецептом")
    publication = models.CharField(max_length=20, choices=PUBLICATION_CHOICES, default='archived', verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название ингредиента')
    calories = models.PositiveIntegerField(blank=True, null=True, verbose_name="Калории")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


