from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news_view, name="news"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("available_currency", views.available_currency_view, name="available_currency"),
    path("saved_conversion", views.saved_conversion_view, name="saved_conversion"),
    path("about", views.about_view, name="about"),
    path("profile", views.profile_view, name="profile"),


    # API endpoints
    path("add_conversion/<str:base_code>/<str:quote_code>/", views.add_conversion, name="add_conversion"),
    path("remove_conversion/<str:base_code>/<str:quote_code>/", views.remove_conversion, name="remove_conversion"),
    path("add_recent_conversion/<str:base_code>/<str:quote_code>/", views.add_recent_conversion, name="add_recent_conversion"),
    path("clear_recent_conversions/", views.clear_recent_conversions, name="clear_recent_conversions"),
    path("get_api_key/", views.get_api_key, name="get_api_key"),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)