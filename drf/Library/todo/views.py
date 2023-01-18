from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from rest_framework.pagination import PageNumberPagination


class ProjectPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ToDoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name']
    pagination_class = ProjectPagination


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_fields = ['for_project', 'create_date', 'update_date', 'author']
    pagination_class = ToDoPagination
