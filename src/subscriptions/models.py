from django.db import models
from django.contrib.auth.models import Group, Permission

# Create your models here.
class Subscriptions(models.Model):
    name = models.CharField(max_length=120)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(Permission, limit_choices_to={"content_type__app_label": "subscriptions"})

    class Meta:
        permissions = [
            ("advanced", "Advanced Perm"),
            ("pro", "Pro Perm"),
            ("basic", "Basic Perm"),
        ]