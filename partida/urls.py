from django.conf.urls import url
from .views import index, PartidaList, PartidaCreate, PartidaUpdate, PartidaDelete, PartidaAPI
urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^listar', PartidaList.as_view(), name='partida_listar'),
    url(r'^$', PartidaList.as_view(), name='partida_listar'),
    url(r'^nuevo$', PartidaCreate.as_view(), name='partida_crear'),
    url(r'^editar/(?P<pk>\d+)/$', PartidaUpdate.as_view(), name='partida_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', PartidaDelete.as_view(), name='partida_eliminar'),
    url(r'^api', PartidaAPI.as_view(), name='api'),
]