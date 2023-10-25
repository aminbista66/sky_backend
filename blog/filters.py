from django_filters import rest_framework as filters
from .models import Blog, ShortNotice

class BlogFilterset(filters.FilterSet):
    topic = filters.CharFilter(field_name="topic", lookup_expr="icontains")
    author = filters.CharFilter(field_name="author", lookup_expr="icontains")

    class Meta:
        model = Blog
        fields = ["topic", "author"]


class shortNoticeFilterset(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    designation = filters.CharFilter(field_name="designation", lookup_expr="icontains")
    issued_by = filters.CharFilter(field_name="issued_by", lookup_expr="icontains")
    content = filters.CharFilter(field_name="content", lookup_expr="icontains")

    class Meta:
        model = ShortNotice
        fields = ["title", "designation", "issued_by", "content"]