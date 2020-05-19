# my_auth/urls.py

from django.urls import path
from django.conf.urls import url

from rest_framework_simplejwt import views as jwt_views
from my_auth import views

urlpatterns = [
    path('token/', views.OleTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserSignUp.as_view(), name='signup'),
    
]

    #url(r'^search/$', views.AttachmentList.as_view(), name='attachment_search'),
    #path('list/<int:pk>/', views.AttachmentRetreiveUpdateDestroy.as_view(), name='attachment_details'),