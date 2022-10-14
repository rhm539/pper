"""pper_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
#from dashboard.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    #path('home/', index)
    #path('dashboard/', views.index, name='dashboard-index'),
    #path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='partials/home.html'), name='home'),
    path('', TemplateView.as_view(template_name='partials/web.html'), name='web'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
         template_name='commons/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='web'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='commons/change-password.html', success_url='/'), name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='commons/password-reset/password_reset.html',
         subject_template_name='commons/password-reset/password_reset_subject.txt', email_template_name='commons/password-reset/password_reset_email.html',), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='commons/password-reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='commons/password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='commons/password-reset/password_reset_complete.html'), name='password_reset_complete'),
    path('setup/', include('setup.urls')),
    path('plan/', include('plan.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
