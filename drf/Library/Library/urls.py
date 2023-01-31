from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='1',
        description='Doc for API',
        contact=openapi.Contact(email='testemail@email.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('Biography', BiographyModelViewSet)
router.register('Book', BookModelViewSet)
router.register('Article', ArticleModelViewSet)
router.register('my', MyAPIView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    # path('api/1/authors', include('authors.urls', namespace='1')),
    # path('api/2/authors', include('authors.urls', namespace='2')),
    # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'})),
    path('api/authors', MyAPIView.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
