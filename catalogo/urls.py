from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticuloListView.as_view(), name='lista'),
    path('nuevo/', views.ArticuloCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.ArticuloDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.ArticuloUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.ArticuloDeleteView.as_view(), name='eliminar'),
]