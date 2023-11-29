from django.urls import path
from .views import BookModelViewSet

app_name = 'books'

urlpatterns = [
    path('', BookModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_list_create_api'),
    path('<int:pk>/', BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='book_retrieve_update_destroy_api'),
]
