from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news_view, name="news"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register")

]