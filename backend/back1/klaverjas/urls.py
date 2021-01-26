# klaverjas/urls.py

from django.urls import path
from django.conf.urls import url

from rest_framework_simplejwt import views as jwt_views

from klaverjas import views

urlpatterns = [
    path('log/click/', views.LogClickView.as_view(), name='log_click'),
    path('log/action/', views.LogActionView.as_view(), name='log_action'),
    path('matches/create/', views.MatchCreate.as_view(), name='match_create'),
    path('matches/list', views.MatchList.as_view(), name='match_list'),
    path('matches/<str:matchID>/', views.MatchRetrieveUpdate.as_view(), name='match_retreive_update'),
    path('remarks/create/', views.RemarkCreate.as_view(), name='remark_create'),
    path('remarks/list', views.RemarkList.as_view(), name='remark_list'),
    # path('remarks/<int:remarkID>/', views.RemarkListCreate.as_view(), name='remark_RU'),
    # path('games/list', views.Game2MatchList.as_view(), name='game_list'),
    path('games/create', views.GameCreate.as_view(), name='game_create'),
    path('games/mail', views.MailToPlayers.as_view(), name='game_mail'),
    url(r'^games/search/$', views.Game2MatchList.as_view(), name='game_list'),
    url(r'^games/score/$', views.GameScore.as_view(), name='game_score'),
    url(r'^games/slagen/$', views.SlagList.as_view(), name='slag_list'),
    path('players/list/', views.PlayerList.as_view(), name='players_list'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/', views.PlayerRetrieveUpdateDestroy.as_view(), name='players_RUD'),
    url(r'^players/search/$', views.PlayerList.as_view(), name='players_list'),
    path('users/<str:username>/', views.UserRetrieve.as_view(), name='user_retreive_update'),
]

