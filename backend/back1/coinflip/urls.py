# coinflip/urls.py

from django.urls import path
from django.conf.urls import url

from rest_framework_simplejwt import views as jwt_views

from coinflip import views

urlpatterns = [
    path('postdata/', views.CoinFlipResultsView.as_view(), name='postdata'),
]