from django.views import View
from django.http import FileResponse
from rest_framework.response import Response
from ..models import Blog

class FileServeView(View):
    def get(self, *args, **kwargs):
        file_slug = kwargs.get("slug")

        if file_slug is None:
            return Response({"message": "File slug not provided"}, status=403)
        try:
            blog = Blog.objects.get(slug=file_slug)
            file_path = "/media/" + blog.get_file_name(blog.id)
            file = open(file_path, "rb")
            return FileResponse(file)
        except:
            raise Exception('Blog not found.')
