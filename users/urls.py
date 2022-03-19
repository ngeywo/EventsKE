from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login-user/',views.login_user, name="login"),
    path('logout-user/', views.logout_user, name= 'logout'),
    path('register-user/', views.register_user, name = 'register'),
    path('profile/', views.profile, name= 'profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),



]