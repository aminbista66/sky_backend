from django.db import models
from django.utils.text import slugify
from .utils import file_validate, mail_validation, get_upload_folder
import uuid
import os

class Blog(models.Model):
    class BlogCategory(models.TextChoices):
        NEWS_AND_ANNOUNCEMENT = "news_and_announcement", "News And Announcement"
        EVENT = "event", "Event"
        GENERAL = "general", "General"
        ACADEMICS = "academics", "Academics"
        PARENTS_RESOURCE = "parents_resource", "Parents Resource"
        CAREER = "career", "Career"
        ACHIEVEMENTS = "acheivements", "Achievements"
        POLICIES = "school_policies_guidelines", "School Policies And Guidelines"
        HEALTH = "health_wellness", "Health and Wellness"
        TECHNOLOGY = "technology", "Technology"
        ARTS = "arts", "Arts"
        SCIENCE = "science", "Science"

    slug = models.CharField(max_length=260, null=True, blank=True)
    topic = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=False, null=False)
    is_approved = models.BooleanField(default=False)
    mail = models.EmailField(null=False, blank=False, validators=[mail_validation])
    file = models.FileField(upload_to=get_upload_folder, validators=[file_validate], null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} | {self.topic[:20]}...'

    def get_file_name(self):
        if self.is_approved:
            return "blogs/approved/" + f"{self.slug}-blog.md"
        return "blogs/unapproved/" + f"{self.slug}-blog.md"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = f"{slugify(self.topic)}" + "-" + str(uuid.uuid4())[:6]
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        self.file.delete(False)
        return super().delete(*args, **kwargs)


class ShortNotice(models.Model):
    title = models.CharField(max_length=64*8, null=False, blank=True)
    content = models.TextField()
    issued_by = models.CharField(max_length=255, null=False, blank=False)
    designation = models.CharField(max_length=255, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title[:20]}.... | {self.issued_by}"