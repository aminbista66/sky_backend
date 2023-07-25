from django.shortcuts import render
from django.views import generic

class DashboardView(generic.TemplateView):
    template_name = "dashboard/index.html"
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})