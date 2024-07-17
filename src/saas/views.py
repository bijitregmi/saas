from django.shortcuts import render
from visits.models import PageVisits
from django.conf import settings
from django.contrib.auth.decorators import login_required

def home_page(request, *args, **kwargs):
    path = request.path
    PageVisits.objects.create(path=path)
    qs = PageVisits.objects.all()
    curret_qs = PageVisits.objects.filter(path=path)
    context = {
        "current_page_visits" : curret_qs.count(),
        "total_page_visits": qs.count(),
    }
    if path == '/about/':
        return render(request, "about.html", context)
    return render(request, "home.html", context)

def about_page(request, *args, **kwargs):
    return home_page(request, *args, **kwargs)

VALID_CODE = '12345'

def pw_protected_view(request, *args, **kwargs):
    context = {}
    is_allowed = request.session.get('protected_page_allowed') or 0
    print(request.session.get('protected_page_allowed'), type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        if request.POST.get("code") == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, 'protected/visit.html', context)
    return render(request, 'protected/entry.html', context)

@login_required
def user_only_view(request, *args, **kwargs):
    return render(request, 'protected/user-only.html', {})