from django.urls import path
from django.contrib.auth import views as auth_views  #for password reset using email
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('' , views.HomePage , name = "home"),
    path('register/' , views.registerPage , name="register"),
    path('login/' , views.loginPage , name = "login"),
    path('logout/' , views.logoutUser , name = "logout"),

    path('reset_password/',
          auth_views.PasswordResetView.as_view(template_name = "authApp/password_reset.html") , name="reset_password"),

     path('password_reset_sent/',
          auth_views.PasswordResetDoneView.as_view(template_name = "authApp/password_reset_send.html") , name="password_reset_done"),

     path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name = "authApp/password_reset_form.html"), name="password_reset_confirm"),

     path('password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name = "authApp/password_reset_done.html"), name="password_reset_complete")

]



