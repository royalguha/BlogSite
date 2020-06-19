from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostCreateView,PostDeletelView,PostUpdateView


urlpatterns = [
    path("",PostListView.as_view(),name="index"),
    path("register",views.register,name="register"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("profile",views.profile,name="profile"),
    path("post/<int:pk>/",PostDetailView.as_view(),name="post-detail"),
    path("post/new",PostCreateView.as_view(),name="post-create"),
    path("post/<int:pk>/delete/",PostDeletelView.as_view(),name="post-delete"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="post-update"),
    path("password_reset", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password-reset"),
    path("password_reset_confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password-reset-confirm"),
    path("password_reset/done", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password-reset"),
]
