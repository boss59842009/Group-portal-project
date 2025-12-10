from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    groups_permissions = {
        "admin": ["add_user", "change_user", "delete_user", "can_edit_all", "can_moderate"],
        "moderator": ["can_moderate"],
        "user": ["change_user"]
    }

    user_ct = ContentType.objects.get_for_model(CustomUser)

    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_name in perms:
            try:
                perm = Permission.objects.get(codename=perm_name, content_type=user_ct)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                pass