from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("", views.home, name="home"),
    path("registration", views.register_request, name="registration"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
