from django.shortcuts import render
from visits.models import PageVisits

def home_page(request, *args, **kwargs):
    path = request.path
    PageVisits.objects.create(path=path)
    qs = PageVisits.objects.all()
    curret_qs = PageVisits.objects.filter(path=path)
    context = {
        "page_title": "My page",
        "current_page_visits" : curret_qs.count(),
        "total_page_visits": qs.count(),
    }
    return render(request, "base.html", context)

def about_page(request, *args, **kwargs):
    return home_page(request, *args, **kwargs)