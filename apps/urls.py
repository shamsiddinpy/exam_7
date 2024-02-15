from django.urls import path

from apps.views import IndexView, AddBlogView, DeleteProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-blog/', AddBlogView.as_view(), name='add_blog'),
    path('delete-blog/<int:pk>/', DeleteProductView.as_view(), name='delete_blog'),
]
