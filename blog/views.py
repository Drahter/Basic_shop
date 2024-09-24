from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogArticle


class BlogArticleListView(ListView):
    model = BlogArticle


class BlogArticleDetailView(DetailView):
    model = BlogArticle

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogArticleCreateView(CreateView):
    model = BlogArticle
    fields = ("title", "content", "preview_image", "is_published", "views_counter")
    success_url = reverse_lazy("blog:blog_list")


class BlogArticleUpdateView(UpdateView):
    model = BlogArticle
    fields = ("title", "content", "preview_image", "is_published", "views_counter")
    success_url = reverse_lazy("blog:blog_list")


class BlogArticleDeleteView(DeleteView):
    model = BlogArticle
    success_url = reverse_lazy("blog:blog_list")
