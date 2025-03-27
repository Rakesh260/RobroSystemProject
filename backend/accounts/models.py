
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('worker', 'Worker'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='captured_images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} by {self.user.username}"


class SupervisorWorkerRelation(models.Model):
    """
    Model to link supervisors with their assigned workers.
    Ensures that a worker is only assigned to one supervisor.
    """
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supervised_workers')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_supervisor')

    class Meta:
        unique_together = ('supervisor', 'worker')

    def __str__(self):
        return f"{self.supervisor.username} supervises {self.worker.username}"


class ActivityLog(models.Model):
    """
    Tracks actions performed by users (e.g., login, role changes, image uploads).
    Useful for monitoring and auditing system activities.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="activity_logs")
    action = models.CharField(max_length=255)  # Example: "Created User", "Assigned Role"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"


class DashboardSummary(models.Model):
    """
    Stores summarized data for dashboards, preventing performance issues with large queries.
    """
    total_users = models.PositiveIntegerField(default=0)
    total_images = models.PositiveIntegerField(default=0)
    total_supervisors = models.PositiveIntegerField(default=0)
    total_workers = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dashboard Summary - {self.last_updated}"


