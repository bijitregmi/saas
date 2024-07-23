from django.contrib import admin

from .models import PageVisits

class PageVisitsAdmin(admin.ModelAdmin):
    list_display =['path', ]

# Register your models here.
admin.site.register(PageVisits, PageVisitsAdmin)