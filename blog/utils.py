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

def file_md_validate(file):
    check_exts = "md"
    file_extension = str(file).split(".")
    print(f'File Extension: {file_extension}')
    if len(file_extension) > 2:
        raise ValidationError("File has multiple extension")
    if file.size >= 10000000:
        raise ValidationError("File should less then 10MB")
    if file_extension[1] == check_exts:
        pass
    else:
        raise ValidationError("Provide Valid Markdown file with .md extension")
    if file:
        pass
    else:
        raise ValidationError("MD File is not provided")

def file_img_validate(file):
    check_exts = ["jpg", "jpeg", "png", "webpg"]
    file_extension = str(file).split(".")
    if len(file_extension) > 2:
        raise ValidationError("File has multiple extension")
    if file.size >= 3000000:
        raise ValidationError("File should less than 3MB")
    if not file_extension[1] in check_exts:
        raise ValidationError("Provide Valid Image file with extension jpeg, jpg, png, webpg")
    if not file:
        raise ValidationError("Image File is not provided")
    pass
        

def get_upload_folder(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.slug}-blog.{ext}"
    return "/".join(["blogs", filename])
