from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView)
from .models import Product, Category
from django.urls import reverse_lazy
from .forms import CategoryCreateForm, ProductCreateForm

class AdminTemplateView(TemplateView):
    template_name='app/admin/html'

class ProductCreateView(CreateView):
        model = Product
        exclude = ['slug', 'create', 'update']
        template_name = 'app/app.html'
        context_object_name = 'products'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total'] = 5
    #     return context

class ProductListView(ListView):
    model = Product
    template_name = 'app/app.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    form = CategoryCreateForm
    template_name = 'app/product_add.html'
    success_url = reverse_lazy('categories')

class CategoryListView(ListView):
    model = Category
    template_name = 'app/categories_html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app/category_detail_html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    form = CategoryCreateForm
    template_name = 'app/category_add.html'
    success_url = reverse_lazy('categories')

