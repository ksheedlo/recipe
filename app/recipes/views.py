import django.http
import django.shortcuts

import recipes.models

def index(request):
    recipes_results = recipes.models.Recipe.objects.order_by('publish_time').reverse()[:20]
    return django.shortcuts.render_to_response('recipes/skillit.html', {
                                                'recipes': recipes_results
                                                })

def detail(request, recipe_id):
    recipe = recipes.models.Recipe.objects.get(id=recipe_id)
    return django.shortcuts.render_to_response('recipes/recipe.html', {
                                                'recipe': recipe
                                                })

def category(request, category_name):
    short_name = recipes.models.recipe_category_shortname(category_name)

    #One-off hack for main meals This could be better from a high level design
    #perspective...
    if category_name == 'main':
        short_name = 'M'
        category_name = 'main meal'
    recipes_results = recipes.models.Recipe.objects.filter(category=short_name).order_by('publish_time').reverse()[:20]
    return django.shortcuts.render_to_response('recipes/category.html', {
                                                'recipes': recipes_results,
                                                'category_name': category_name
                                                })
