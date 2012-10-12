from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^recipe/$", 'recipes.views.index'),
    url(r"^recipe/(?P<recipe_id>\d+)/$", 'recipes.views.detail'),
    url(r"^recipe/category/(?P<category_name>\w+)/$", 'recipes.views.category'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
