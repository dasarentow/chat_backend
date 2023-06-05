"""project URL Configuration

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
# from . jwt import MyTokenObtainPairView as MyMyTokenObtainPairView
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.schemas import get_schema_view
from .views import *
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(
    title="Pastebin API",
)


# schema_url_patterns = [
#     path('', include('project.urls')),
# ]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # path('api /users/', include('users.urls')),
    path("api/users/", include("myusers.urls", namespace="myusers")),
    path("auth/", include("djoser.urls")),
    path("auth/token/", include("djoser.urls.authtoken")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("docs/", include_docs_urls(title="BlogAPI")),
    path(
        "schema-project",
        get_schema_view(
            title="BlogAPI",
            description="API for the Blog Project",
            version="1.0.0",
            urlconf="project.urls",
        ),
        name="openapi-schema",
    ),
    path(
        "schema-blog",
        get_schema_view(
            title="BlogAPI",
            description="API for the Blog Project",
            version="1.0.0",
            urlconf="blog.api.urls",
            #  patterns=schema_url_patterns,
        ),
        name="openapi-schema",
    ),
    path(
        "schema",
        get_schema_view(
            title="BlogAPI",
            description="API for the Blog Project",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    # apps
    path("api/", include("chat.urls", namespace="chat")),
    path("api/", include("dsapps.urls", namespace="dsapps")),
    path("drf-swagger", schema_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
