from django.http import HttpResponse
from recipes.views import home
from django.urls import path, include


urlpatterns = [
    path('', home), #home
]
