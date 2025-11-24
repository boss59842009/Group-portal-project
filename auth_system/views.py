from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from .models import CustomUser

# Create your views here.
class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "auth_system/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "auth_system/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = ("auth_system/profile.html")

    def get_object(self):
        return self.request.user

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "auth_system/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user