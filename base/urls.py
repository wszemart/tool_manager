"""
URL configuration for tool_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import environ
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users.views import LogoutUser, NewUserRegister, UserProfile

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

DEBUG = env("DEBUG")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("machines.urls")),
    path("", include("tools_assembly.urls")),
    path("", include("tools.urls")),
    path("", include("holders.urls")),
    path("", include("notifications.urls")),
    path("register/", NewUserRegister.as_view(), name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("i18n/", include("django.conf.urls.i18n")),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
