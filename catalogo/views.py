from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Articulo
from .forms import ArticuloForm

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'catalogo/lista.html'
    context_object_name = 'articulos'
    def get_queryset(self):
        return Articulo.objects.select_related('categoria').all()

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'catalogo/detalle.html'
    context_object_name = 'articulo'

class ArticuloCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = "Artículo creado correctamente"

class ArticuloUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = "Artículo actualizado correctamente"

class ArticuloDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Articulo
    template_name = 'catalogo/confirmar_eliminar.html'
    success_url = reverse_lazy('lista')
    success_message = "Artículo eliminado correctamente "