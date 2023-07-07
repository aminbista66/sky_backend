app_name = "blog"

from django.urls import path
from .views.blogs_views import BlogListAPIView, BlogRetrieveUpdateDestroyAPIView, BlogCreateAPIView
from .views.serve_file_views import FileServeView

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog-lists"),
    path("create/", BlogCreateAPIView.as_view(), name="blog-create"),
    path(
        "<slug:slug>/",
        BlogRetrieveUpdateDestroyAPIView.as_view(),
        name="blog-retrieve-update-destroy",
    ),
    path("/md/<slug:slug>/", FileServeView.as_view(), name="file-serve")
]
