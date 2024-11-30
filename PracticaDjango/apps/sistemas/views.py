from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from PracticaDjango.apps.sistemas.forms import RequestDemoForm


# Create your views here.

class IndexHomeView(TemplateView):
    template_name = "home/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("panel_home")  # Redirige al login si no está logueado
        return super().dispatch(request, *args, **kwargs)


def panel(request):
    context = {}
    return render(request, "panel_home.html", context)

