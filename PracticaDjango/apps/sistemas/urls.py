from django.urls import path
from django.contrib.auth.decorators import login_required

from PracticaDjango.apps.sistemas.views import IndexHomeView, panel

urlpatterns = [
    path('', IndexHomeView.as_view(), name="index_home"),
    path('panel/', login_required(panel), name="panel_home"),
]