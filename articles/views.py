from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #these have to proceed CreateView..etc to be read first
from django.views.generic import ListView, DetailView , CreateView
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy 
from .models import Article
from django.shortcuts import render

# Create your views here.

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title' , 'body',)
    template_name = 'create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
