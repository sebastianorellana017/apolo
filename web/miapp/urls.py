from django.urls import path, include
from miapp.views import Home, registro
from django.contrib.auth import views as auth_views
from miapp import views


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('pagina/', views.pagina, name='pagina'),
]