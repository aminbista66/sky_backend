from rest_framework import generics
from ..serializers import BlogListSerializer
from rest_framework import permissions
from ..models import Blog


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Blog.objects.filter(is_approved=True)


class BlogCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]


class BlogRetrieveUpdateDestroyAPIView(
    generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = BlogListSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]
