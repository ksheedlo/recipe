import json

from django.db import models

RECIPE_CATEGORY_CHOICES = (
    ('A', 'appetizer'),
    ('C', 'cocktail'),
    ('D', 'dessert'),
    ('M', 'main meal'),
    ('S', 'side'),
)

def recipe_category_shortname(long_name):
    for (sn, ln) in RECIPE_CATEGORY_CHOICES:
        if ln == long_name:
            return sn
    return ''

RECIPE_DEFAULT_PHOTO = '/static/photos/skillit_default.png'

class Ingredient(models.Model):
    quantity = models.CharField(max_length=32)
    item = models.CharField(max_length=64)
    unit = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return '{0} {1}{2} {3}'.format(
            self.quantity,
            self.unit,
            's' if self.unit != '' and self.parse_quantity() > 1 else '',
            self.item
            )

    def parse_quantity(self):
        try:
            return float(self.quantity)
        except ValueError:
            pass

        split_str = self.quantity.replace('/', ' ')
        chars = split_str.split(' ')
        while '' in chars:
            chars.remove('')

        split = [float(num) for num in chars]
        if len(split) == 1:
            return split[0]
        elif len(split) == 2:
            return split[0] / split[1]
        else:
            return split[0] + split[1] / split[2]

class Recipe(models.Model):
    name = models.CharField(max_length = 64)
    ingredients = models.ManyToManyField(Ingredient)
    procedure = models.CharField(max_length = 1024)
    servings = models.IntegerField()
    description = models.CharField(max_length = 1024)
    category = models.CharField(max_length=1, choices=RECIPE_CATEGORY_CHOICES)
    publish_time = models.DateTimeField(auto_now_add = True)
    photo = models.CharField(max_length = 64)

    def __unicode__(self):
        return self.name

    def get_photo_or_default():
        import pdb; pdb.set_trace()
        if photo is None:
            return RECIPE_DEFAULT_PHOTO
        if recipe.photo.strip() == '':
            return RECIPE_DEFAULT_PHOTO
        return '/static/photos/'+recipe.photo

class Review(models.Model):
    # TODO: There should be some notion of a user account so people can't just
    #       come in and spam negative reviews, etc.

    title = models.CharField(max_length = 64)
    user_name = models.CharField(max_length = 64)
    recipe = models.ForeignKey(Recipe)
    rating = models.IntegerField()
    text = models.CharField(max_length = 1024)
    publish_time = models.DateTimeField(auto_now_add = True)

