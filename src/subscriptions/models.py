from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

ALLOW_CUSTOM_GROUPS =True

SUBSCRIPTION_PERMISSIONS = [
            ("advanced", "Advanced Perm"),
            ("pro", "Pro Perm"),
            ("basic", "Basic Perm"),
        ]

# Create your models here.
class Subscriptions(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=120)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(Permission, limit_choices_to={
        "content_type__app_label": "subscriptions",
        "codename__in": [x[0] for x in SUBSCRIPTION_PERMISSIONS]
        })

    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS
        verbose_name = 'Subscription'

    def __str__(self):
        return f'{self.name}'
    
    
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscriptions, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s plan: {self.subscription}"
    
@receiver(post_save, sender=UserSubscription)
def add_groups_to_users(sender, instance, **kwargs):
    user_sub_instance = instance
    subscription_obj = user_sub_instance.subscription
    user = user_sub_instance.user
    group_ids = []
    if subscription_obj is not None:
        groups = instance.subscription.groups.all()
        group_ids = groups.values_list('id', flat=True)
    if not ALLOW_CUSTOM_GROUPS:
        user.groups.set(group_ids)
    else:
        subs_qs = Subscriptions.objects.filter(active=True)
        if subscription_obj is not None:
            subs_qs = subs_qs.exclude(id=subscription_obj.id)
        subs_groups = subs_qs.values_list("group__id", flat=True)
        subs_groups_set = set(subs_groups)
        current_groups = user.groups.all().values_list("id", flat=True)
        groups_id_set = set(group_ids)
        current_groups_set = set(current_groups) - subs_groups_set
        final_group_set = list(groups_id_set | current_groups_set)
        user.groups.set(final_group_set)