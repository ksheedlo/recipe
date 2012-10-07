from django.db import models

INGREDIENT_FORMAT_CHOICES = (
    ('D', 'decimal'),
    ('R', 'rational'),
)

class Ingredient(models.Model):
    quantity = models.CharField(max_length=32)
    item = models.CharField(max_length=64)
    unit = models.CharField(max_length=64)
    ingredient_format = models.CharField(max_length=1, 
                                        choices = INGREDIENT_FORMAT_CHOICES)

class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    procedure = models.CharField(max_length = 1024)
    photo = models.CharField(max_length = 64)

class Review(models.Model):
    # TODO: There should be some notion of a user account so people can't just
    #       come in and spam negative reviews, etc.

    user_name = models.CharField(max_length = 64)
    recipe = models.ForeignKey(Recipe)
    rating = models.IntegerField()
    text = models.CharField(max_length = 1024)
