from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create a default admin user if it doesn't exist"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123",
                role="admin"
            )
            self.stdout.write(self.style.SUCCESS("Default admin user created successfully!"))
        else:
            self.stdout.write(self.style.SUCCESS("Admin user already exists."))
