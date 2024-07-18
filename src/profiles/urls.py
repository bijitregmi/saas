from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles_list_view),
    path('<username>/', views.profile_detail_view, name='profile')
]
