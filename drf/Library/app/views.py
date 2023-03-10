from flask import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer, \
    AuthorModelSerializer2
from rest_framework.pagination import LimitOffsetPagination


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name']
    pagination_class = AuthorPaginator

    # # Через query параметры
    # def get_queryset(self):
    #     param = self.request.query_params.get('name')
    #     if param:
    #         return Author.objects.filter(first_name__contains=param[0])
    #     return super().get_queryset()


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class MyAPIView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorModelSerializer
        return AuthorModelSerializer2
