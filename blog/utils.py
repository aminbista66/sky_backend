import os
import uuid
from django.core.exceptions import ValidationError

VALID_DOMAIN = "skyrider.edu.np"

def mail_validation(mail):
    initial, domain = mail.split("@")
    if len(initial) < 4:
        raise ValidationError("Invalid Mail")
    if domain != VALID_DOMAIN:
        raise ValidationError("Invalid Mail")

def file_validate(file):
    check_exts = (".md")
    file_extension= os.path.splitext(str(file))
    if file.size >= 10000000:
        raise ValidationError("File should less then 10MB")
    if file_extension[1] == check_exts[0] or file_extension[1] == check_exts[1] or file_extension[1] == check_exts[2]:
        pass
    else:
        raise ValidationError("Provide Valid Markdown file with .md extension")
    if file:
        pass
    else:
        raise ValidationError("MD File is not provided")

def get_upload_folder(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.id}-blog.{ext}"
    if instance.is_approved:
        return "/".join(["blogs", "unapproved", filename])
    return "/".join(["blogs", "approved", filename])