from django.views.generic import ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
