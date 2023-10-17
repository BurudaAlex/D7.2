from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    ordering = '-title',
    template_name = 'PostCategory.html'
    context_object_name ='PostCategory'
    paginate_by = 3  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'PostCategoryOneByOne.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'PostCategoryOneByOne'



