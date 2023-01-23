from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from app.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyAPIView

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('Biography', BiographyModelViewSet)
router.register('Book', BookModelViewSet)
router.register('Article', ArticleModelViewSet)
router.register('my', MyAPIView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('myapi/', MyAPIView.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
