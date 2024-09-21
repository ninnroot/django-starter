"""
URL configuration for simbolo_mta_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_yasg import openapi
from django.conf import settings
import debug_toolbar
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="REST API",
        default_version="v0",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path(
                      "api/v1/swagger/",
                      schema_view.with_ui("swagger", cache_timeout=0),
                      name="schema-swagger-ui",
                  ),
                  path("api/v1/", include("app_auth.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
