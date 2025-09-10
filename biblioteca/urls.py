from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # URLs para Usuario
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/novo/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/<int:pk>/editar/', views.usuario_edit, name='usuario_edit'),
    path('usuarios/<int:pk>/excluir/', views.usuario_delete, name='usuario_delete'),
    
    # URLs para Titulo
    path('titulos/', views.titulo_list, name='titulo_list'),
    path('titulos/novo/', views.titulo_create, name='titulo_create'),
    path('titulos/<int:pk>/', views.titulo_detail, name='titulo_detail'),
    path('titulos/<int:pk>/editar/', views.titulo_edit, name='titulo_edit'),
    path('titulos/<int:pk>/excluir/', views.titulo_delete, name='titulo_delete'),
    
    # URLs para Exemplar
    path('exemplares/', views.exemplar_list, name='exemplar_list'),
    path('exemplares/novo/', views.exemplar_create, name='exemplar_create'),
    path('exemplares/<int:pk>/', views.exemplar_detail, name='exemplar_detail'),
    path('exemplares/<int:pk>/editar/', views.exemplar_edit, name='exemplar_edit'),
    path('exemplares/<int:pk>/excluir/', views.exemplar_delete, name='exemplar_delete'),
    
    # URLs para Emprestimo
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/novo/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/<int:pk>/', views.emprestimo_detail, name='emprestimo_detail'),
    path('emprestimos/<int:pk>/editar/', views.emprestimo_edit, name='emprestimo_edit'),
    path('emprestimos/<int:pk>/excluir/', views.emprestimo_delete, name='emprestimo_delete'),
    path('emprestimos/<int:pk>/devolver/', views.emprestimo_devolver, name='emprestimo_devolver'),
]

