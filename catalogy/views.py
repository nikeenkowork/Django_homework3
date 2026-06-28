from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


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
