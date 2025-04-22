from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('deletar/<int:id>/', views.deletar_curso, name='deletar_curso'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

