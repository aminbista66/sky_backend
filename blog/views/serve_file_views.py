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
            try:
                file_path = "/media/" + blog.get_file_name()
                file = open(str(settings.BASE_DIR) + "/" + file_path, "rb")
            except:
                raise Exception("Cannot open file")
            return FileResponse(file)
        except:
            raise Exception('Blog not found.')