from django.urls import path
from app.views import MyAPIView

app_name = 'authors'
urlpatterns = [
    path('', MyAPIView.as_view())
]
