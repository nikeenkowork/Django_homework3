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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .models import Product
from .forms import ProductForm


class HomeView(View):
    def get(self, request):
        return HttpResponse("Главная страница работает")


# Доступен всем
class ProductListView(ListView):
    model = Product
    template_name = "catalogy/product_list.html"
    context_object_name = "products"


# Доступен всем
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalogy/product_detail.html"
    context_object_name = "product"


class ContactsView(TemplateView):
    template_name = "catalogy/contacts.html"


# Только авторизованные пользователи
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogy/product_form.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Только авторизованные пользователи
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogy/product_form.html"
    success_url = reverse_lazy("product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)

        if product.owner != self.request.user:
            raise Http404

        return product


# Только авторизованные пользователи
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalogy/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)

        if (
                product.owner != self.request.user
                and not self.request.user.has_perm(
            "catalogy.can_unpublish_product"
        )
        ):
            raise Http404

        return product


# Только пользователи с правом can_unpublish_product
@permission_required("catalogy.can_unpublish_product")
def unpublish_product(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    product.is_published = False
    product.save()

    return redirect(
        "product_detail",
        pk=pk
    )
