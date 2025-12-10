from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    groups_permissions = {
        "admin": ["add_user", "change_user", "delete_user",
            "can_edit_all", "can_moderate"],
        "moderator": ["can_moderate"],
        'user': ["change_user"]
    }

    for group_name, perm in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_name in perm:
            try:
                new_perm = Permission.objects.get(code_name=perm_name)
                group.permissions.add(new_perm)
            except Permission.DoesNotExist:
                pass