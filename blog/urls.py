app_name = "blog"

from django.urls import path
from .views.blogs_views import BlogListAPIView, BlogUpdateDestroyAPIView, BlogCreateAPIView, BlogRetrieveAPIView
from .views.serve_file_views import FileServeView
from .views.shortnotice_views import ShortNoticeListAPIView, ShortNoticeCreateAPIView, ShortNoticeUpdateDestroyAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog-lists"),
    path("create/", BlogCreateAPIView.as_view(), name="blog-create"),
    path(
        "<slug:slug>/",
        BlogUpdateDestroyAPIView.as_view(),
        name="blog-update-destroy",
    ),
    path(
        "detail/<slug:slug>/",
        BlogRetrieveAPIView.as_view(),
        name="blog-update-destroy",
    ),
    path("notices/", ShortNoticeListAPIView.as_view(), name="shortnotice-list"),
    path("notice/create/", ShortNoticeCreateAPIView.as_view(), name="shortnotice-create"),
    path("notice/<int:pk>/", ShortNoticeUpdateDestroyAPIView.as_view(), name="shortnotice-update-destroy"),
    path("md/<slug:slug>/", FileServeView.as_view(), name="file-serve")
]
