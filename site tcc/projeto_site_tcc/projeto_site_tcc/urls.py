from django.urls import path
from app_site_tcc import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('',views.home,name='home'),

    path('comentarios/',views.comentarios,name='listagem_comentarios')
]
