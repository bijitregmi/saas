from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required
def profile_view(request, username=None, *args, **kwargs):
    current_user = request.user
    profile_of_user = get_object_or_404(User, username=username)
    return HttpResponse(f"Hello {username} Id = {profile_of_user.id}")