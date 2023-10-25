app_name = "dashboard"

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="index"),
    path('login/', LoginView.as_view(template_name="dashboard/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]