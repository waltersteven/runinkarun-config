from django.conf.urls import url
from .views import ScoreList, ScoreAPI

urlpatterns = [
    url(r'^$', ScoreList.as_view(), name='score_listar'),
    url(r'^api', ScoreAPI.as_view(), name='api')
]