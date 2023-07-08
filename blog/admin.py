from django.contrib import admin
from .models import Blog, ShortNotice

class BlogModelAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "topic",
        "author",
        "is_approved",
        "mail",
        "created_at",
        "updated_at"
    )

class NoticeModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "issued_by",
        "designation",
        "created_at",
        "updated_at",
    )

admin.site.register(Blog, BlogModelAdmin)
admin.site.register(ShortNotice, NoticeModelAdmin)