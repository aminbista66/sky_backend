from django.db import models
from django.utils.text import slugify
from .utils import file_validate, mail_validation
import uuid

class Blog(models.Model):
    slug = models.CharField(max_length=260, null=True, blank=True)
    topic = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to="blog_md/", validators=[file_validate], null=False, blank=False)
    is_approved = models.BooleanField(default=False)
    mail = models.EmailField(null=False, blank=False, validators=[mail_validation])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} | {self.topic[:20]}...'

    def get_file_name(self):
        if self.is_approved:
            return "blogs/approved/" + f"{self.id}-blog.md"
        return "blogs/unapproved/" + f"{self.id}-blog.md"

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.topic)}" + str(uuid.uuid4()[:-4])
        return super().save(*args, **kwargs)