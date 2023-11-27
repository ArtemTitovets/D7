from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from datetime import datetime

from .filters import PostFilter

from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


# Добавляем новое представление для создания товаров.
class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news_search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ArticlesCreate(CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'article'
        return super().form_valid(form)


class NewsCreate(CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'news'
        return super().form_valid(form)


class ArticlesUpdate(UpdateView):
    permission_required = ('news.change_post',)
    model = Post
    fields = ['author', 'heading', 'text']
    template_name = 'articles_update.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'article'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    permission_required = ('news.change_post',)
    model = Post
    fields = ['author', 'heading', 'text']
    template_name = 'news_update.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'news'
        return super().form_valid(form)


class ArticlesDelete(DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'article'
        return super().form_valid(form)


class NewsDelete(DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.post_type = 'news'
        return super().form_valid(form)
