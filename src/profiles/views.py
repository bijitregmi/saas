from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profiles_list_view(request, *args, **kwargs):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, 'profiles/list.html', context)

# Create your views here.
@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    current_user = request.user
    profile_of_user = get_object_or_404(User, username=username)
    is_me = current_user == profile_of_user
    context = {
        'owner' : is_me,
        'instance' : profile_of_user
    }
    return render(request, 'profiles/detail.html', context)