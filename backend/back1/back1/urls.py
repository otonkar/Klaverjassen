from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt import views as jwt_views

from my_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('my_auth.urls')),
    path('klaverjas/', include('klaverjas.urls')),
    path('coinflip/', include('coinflip.urls')),
    path('wheel/', include('wheel.urls')),
    path('test/', views.Test.as_view(), name='test'),
]