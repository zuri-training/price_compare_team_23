from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from .views import register , signin

app_name = "accounts"

urlpatterns = [
    path("signup/", views.register, name="signUp"),
    path("login/", signin, name="signin"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"
    ),
    # path(
    #     "reset_password_sent/",
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    #),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
]
