from django.contrib.auth.forms import UserCreationForm

from dashboard.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
        ]
