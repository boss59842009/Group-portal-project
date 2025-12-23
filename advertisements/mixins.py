from django.core.exceptions import PermissionDenied


class AdvertisementManagePermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            raise PermissionDenied

        if not user.can_manage_advertisements():
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)