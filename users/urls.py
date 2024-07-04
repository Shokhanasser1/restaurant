from django.urls import path
from .views import *

from django.views.generic import TemplateView

urlpatterns = [
    path('profile/', profile_page, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('logout/', logout_view, name='logout'),
    
]
