from rest_framework import serializers
from .models import Blog, ShortNotice

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "slug",
            "topic",
            "author",
            "is_approved",
            "mail",
            "created_at",
            "updated_at",
        )

class ShortNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortNotice
        fields = "__all__"