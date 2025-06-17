from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from . import views

urlpatterns = [
    path("signup/", views.UserCreateAndLoginView.as_view(), name="signup"),
    path(
        "login/",
        LoginView.as_view(
            redirect_authenticated_user=True, template_name="accounts/login.html"
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user_detalle/<int:pk>/", views.UserDetail.as_view(), name="user_detalle"),
    path("user_update/<int:pk>/", views.UserUpdate.as_view(), name="user_update"),
    path("cambiar_contraseña/", views.PasswordChange.as_view(), name="cambiar_contraseña"),
    path(
        "cambiar_contraseña/done/",
        views.PasswordChangeDone.as_view(),
         name="password_change_done",  
    ),
    path("user_delete/<int:pk>/", views.UserDelete.as_view(), name="user_delete"),
    
    # URLs para restablecer contraseña
    path(
        "password_reset/", 
        PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt"
        ), 
        name="password_reset"
    ),
    path(
        "password_reset/done/", 
        PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ), 
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/", 
        PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ), 
        name="password_reset_confirm"
    ),
    path(
        "reset/done/", 
        PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ), 
        name="password_reset_complete"
    ),
]