from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news_view, name="news"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("available_currency", views.available_currency_view, name="available_currency"),
    path("saved_currency", views.saved_currency_view, name="saved_currency"),


    # API route
    path("add_currency/<str:base_currency_code>/<str:quote_currency_code>/", views.add_wishlist, name="add_currency"),
    path("remove_currency/<str:base_currency_code>/<str:quote_currency_code>/", views.remove_wishlist, name="remove_currency"),

]