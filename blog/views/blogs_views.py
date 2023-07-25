from rest_framework import generics
from ..serializers import BlogListSerializer, BlogCreateSerializer
from rest_framework import permissions
from ..models import Blog
from ..filters import BlogFilterset


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = BlogFilterset

    def get_queryset(self):
        return Blog.objects.filter(is_approved=True)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class BlogCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = [permissions.AllowAny]

class BlogRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BlogListSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Blog.objects.filter(is_approved=True)


class BlogUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BlogCreateSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Blog.objects.filter(is_approved=True)
