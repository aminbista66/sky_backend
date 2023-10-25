from django.views import View
from django.http import FileResponse
from rest_framework.response import Response
from ..models import Blog
from django.conf import settings

class FileServeView(View):
    def get(self, *args, **kwargs):
        file_slug = kwargs.get("slug")

        if file_slug is None:
            return Response({"message": "File slug not provided"}, status=403)
        try:
            blog = Blog.objects.get(slug=file_slug)
            print(blog)
            if not blog.is_approved:
                raise Exception("blog is not approved")
            try:
                file_path = "/media/" + blog.get_file_name()
                print(file_path)
                file = open(str(settings.BASE_DIR) + "/" + file_path, "rb")
            except:
                raise Exception("Cannot open file")
            return FileResponse(file)
        except:
            raise Exception('Blog not found.')

class ThumbnailServeView(View):
    def get(self, *args, **kwargs):
        file_name = kwargs.get("img")
        if file_name is None:
            return Response({"message": "file name not specified."})
        try:
            file_path = f"/media/thumbnails/{file_name}"
            file = open(str(settings.BASE_DIR) + "/" + file_path, "rb")
        except:
            raise Exception("Cannot open file")
        return FileResponse(file)