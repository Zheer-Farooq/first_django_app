"""
URL configuration for first_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'), # This line maps the URL to the register view
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'), # This line maps the URL to the login view
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),  # This line maps the URL to the logout view
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='password_reset'), # This line maps the URL to the password_reset view
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'), # This line maps the URL to the password_reset_done view
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'), # This line maps the URL to the password_reset_confirm view
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'), # This line maps the URL to the password_reset_complete view
    path('profile/', user_views.profile, name='profile'), # This line maps the URL to the profile view
    path('', include('blog.urls')), # include() function allows referencing other URLconfs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This line is used to serve the media files in development mode

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)