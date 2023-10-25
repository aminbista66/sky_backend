from rest_framework import serializers
from .models import Blog, ShortNotice

class BlogListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField(read_only=True)
    file = serializers.SerializerMethodField(read_only=True)

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
            "thumbnail",
            "file",
        )
    def get_thumbnail(self, obj: Blog):
        request = self.context["request"]
        scheme = request.is_secure() and "https" or "http"
        server_location = f"{scheme}://{request.get_host()}"
        file_slug = str(obj.thumbnail).split("/")[1]
        file_location = f"{server_location}/blogs/thumbnail/{file_slug}"
        return file_location

    def get_file(self, obj: Blog):
        request = self.context["request"]
        scheme = request.is_secure() and "https" or "http"
        server_location = f"{scheme}://{request.get_host()}"
        file_slug = str(obj.slug)
        file_location = f"{server_location}/blogs/md/{file_slug}"
        return file_location

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class ShortNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortNotice
        fields = "__all__"