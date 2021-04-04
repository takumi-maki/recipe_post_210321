from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'description']
    success_url = reverse_lazy('recipe:index')

    def form_valid(self, form):
        messages.success(self.request, '保存しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存できませんでした。')
        return super().form_invalid(form)


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content', 'description']

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('recipe:detail', kwargs={'pk': pk})

    # 保存成功
    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    # 保存失敗
    def form_invalid(self, form):
        messages.error(self.request, '更新できませんでした。')
        return super().form_invalid(form)


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました。')
        return super().delete(request, *args, **kwargs)
