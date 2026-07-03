from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm


class HomeView(View):
    def get(self, request):
        return HttpResponse("Главная страница работает")


class ProductListView(ListView):
    model = Product
    template_name = "catalogy/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalogy/product_detail.html"
    context_object_name = "product"


class ContactsView(TemplateView):
    template_name = "catalogy/contacts.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogy/product_form.html"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogy/product_form.html"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalogy/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")
