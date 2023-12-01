from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import UserCustomViewSet, RegisterUserAPIView
from books.views import BookModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",
        default_version='0.1',
        description="API for managing books in a library",
        contact=openapi.Contact(email="grebenev-81@mail.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

router = DefaultRouter()
router.register('users_for_staff', UserCustomViewSet)
router.register('books', BookModelViewSet)



urlpatterns = [
    path('', lambda request: redirect('/swagger/')),
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
    path('api/users/register/', RegisterUserAPIView.as_view(), name='register_user'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),

    # Other URL patterns
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # Documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from django.conf.urls.static import static
from . import conf_prod
urlpatterns += static(conf_prod.STATIC_URL, document_root=conf_prod.STATIC_ROOT)
