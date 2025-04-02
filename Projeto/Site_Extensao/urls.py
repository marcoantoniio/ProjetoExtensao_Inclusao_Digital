from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inicio/', views.inicio, name='inicio')
]

