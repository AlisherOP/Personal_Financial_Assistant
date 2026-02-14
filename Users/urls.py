from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from users import views

urlpatterns = [
    path("login/", views.user_login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="Users/logout.html"), name="logout"),
    path('', views.index, name="index"),
    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="Users/password_change.html", http_method_names=['post', 'get']), name="password"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="Users/password_change_done.html"), name="password_change_done"),
    # password reset
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="Users/password_reset.html"), name="password_reset")
]
