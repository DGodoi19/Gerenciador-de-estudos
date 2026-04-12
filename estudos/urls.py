from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('trilha/<int:id>/', views.detalhes_trilha, name='detalhes_trilha'),
    path('trilha/<int:trilha_id>/criar_topico/',
         views.criar_topico, name='criar_topico'
         ),
    path('topico/<int:topico_id>/concluir/',
         views.marcar_como_concluido, name='marcar_como_concluido'
         ),
    path('trilha/<int:id>/excluir/',
        views.excluir_trilha, name='excluir_trilha'
        ),
    path('topico/<int:topico_id>/excluir/',
        views.excluir_topico, name='excluir_topico'
        ),
    path('trilha/<int:id>/editar/',
        views.editar_trilha, name='editar_trilha'
        ),
]
