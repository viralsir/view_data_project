"""view_data_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from users import  views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('blog/',include('blog.urls')),
    path("flights/",include('flights.urls')),
    path('register/',user_view.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path("profile/",user_view.profileview,name="profile"),
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="reset_password"),
    path("password_reset/done",auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset_complete",auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete")
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)