import django.http
import django.shortcuts

import recipes.models

def index(request):
    recipes_results = recipes.models.Recipe.objects.order_by('publish_time').reverse()[:20]
    return django.shortcuts.render_to_response('recipes/skillit.html', {
                                                'recipes': recipes_results
                                                })

def recipe(request, recipe_id):
    pass
