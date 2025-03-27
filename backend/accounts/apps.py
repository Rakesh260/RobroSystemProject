from django.apps import AppConfig
from django.core.management import call_command


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """Run command to create default admin user on startup"""
        call_command('create_admin')



