from django.urls import path
from .import views
urlpatterns= [
    path('', views.index, name='index'),
    path('listado', views.listado, name='listado'),
    path('crear', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar')
]