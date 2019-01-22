from django.views.generic import TemplateView
from shared_resources import alerts


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get("alert"):
            context["alert"] = alerts.get(self.request.GET.get("alert"))
        return context