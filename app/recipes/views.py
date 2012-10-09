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
