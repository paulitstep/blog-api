from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', views.BlackListTokenView.as_view(), name='blacklist'),
]