"""masterklass URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import django


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


def custom_server_error(request):
    return django.views.defaults.server_error(request)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('purchase/', include('purchase.urls')),
    path('courses/', include('courses.urls')),
    path('profiles/', include('profiles.urls')),
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
