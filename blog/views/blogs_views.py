from rest_framework import generics
from ..serializers import BlogListSerializer
from rest_framework import permissions
from ..models import Blog
from ..filters import BlogFilterset


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = BlogFilterset

    def get_queryset(self):
        return Blog.objects.filter(is_approved=True)


class BlogCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]

class BlogRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BlogListSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]


class BlogUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BlogListSerializer
    lookup_field = "slug"
    permission_classes = [permissions.IsAdminUser]
