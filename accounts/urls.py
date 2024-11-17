from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
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
        name="cambiar_contraseña_done",
    ),
    path("user_delete/<int:pk>/", views.UserDelete.as_view(), name="user_delete"),
]