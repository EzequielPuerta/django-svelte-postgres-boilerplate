import os
from pathlib import Path

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from api.models import UploadedFile

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    help = "Create user groups and assign permissions"

    def handle(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        content_type = ContentType.objects.get_for_model(UploadedFile)
        permissions = Permission.objects.filter(content_type=content_type)

        admin_group, _ = Group.objects.get_or_create(name="admin")
        admin_group.permissions.set(permissions)

        maintainer_group, _ = Group.objects.get_or_create(name="maintainer")
        maintainer_group.permissions.set(
            permissions.filter(
                codename__in=[
                    "view_uploadedfile",
                    "add_uploadedfile",
                    "change_uploadedfile",
                ]
            )
        )

        client_group, _ = Group.objects.get_or_create(name="client")
        client_group.permissions.set(
            permissions.filter(codename__in=["view_uploadedfile"])
        )

        token_file_name = os.getenv("BROWSER_TOKEN_FILE")
        if token_file_name:
            browser_username = os.getenv("BROWSER_USERNAME", "browser")
            browser_password = os.getenv("BROWSER_PASSWORD", "browserpassword")
            token_file = os.path.join(
                BASE_DIR,
                "browser_token",
                token_file_name,
            )

            browser_user, created = User.objects.get_or_create(
                username=browser_username
            )
            if created:
                browser_user.set_password(browser_password)
                browser_user.save()
                browser_user.groups.add(client_group)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'User "{browser_username}" created and asigned to client group.'
                    )
                )

            token, _ = Token.objects.get_or_create(user=browser_user)
            with open(token_file, "w") as f:
                f.write(token.key)

        self.stdout.write(
            self.style.SUCCESS("Groups created and permissions assigned successfully.")
        )
