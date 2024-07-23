from django.contrib import admin
from .models import Subscriptions, UserSubscription

class SubcriptionAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'permissions')
    list_display = ['name', ]

# Register your models here.
admin.site.register(Subscriptions, SubcriptionAdmin)
admin.site.register(UserSubscription)