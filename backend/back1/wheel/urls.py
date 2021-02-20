# coinflip/urls.py

from django.urls import path
from django.conf.urls import url

from rest_framework_simplejwt import views as jwt_views

from wheel import views

urlpatterns = [
    path('settings/', views.WheelSettingsListCreateView.as_view(), name='wheels_list_create_'),
    path('settings/<int:ID>/', views.WheelSettingsRetreiveUpdateDeleteView.as_view(), name='wheels_RUD'),
]