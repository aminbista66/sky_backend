from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .froms import UserCreateForm
from .mixins import IsStaffMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, IsStaffMixin, generic.TemplateView):
    template_name = "dashboard/index.html"
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})
    
class CreateUserView(LoginRequiredMixin, IsStaffMixin, generic.CreateView):
    form_class = UserCreateForm
    template_name = "dashboard/create_user.html"
    success_url = reverse_lazy("dashboard:home")