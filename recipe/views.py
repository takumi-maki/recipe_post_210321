from django.views.generic import ListView, DetailView
from .models import Recipe
from comment.forms import CommentForm


class RecipeListView(ListView):
    model = Recipe

    def get_queryset(self):
        qs = Recipe.objects.all()
        keyword = self.request.GET.get("q")

        if keyword:
            qs = qs.filter(title__contains=keyword)
        return qs


class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CommentForm'] = CommentForm(initial={'recipe': self.object})
        return context
