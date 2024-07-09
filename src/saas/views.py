from django.shortcuts import render

def home_page(request, *args, **kwargs):
    context = {
        "page_title": "My page"
    }
    return render(request, "base.html", context)