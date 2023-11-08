from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class IsStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied