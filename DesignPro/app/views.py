from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.


def index(request):
    return render(
        request,
        'index.html',
    )


class BBLoginView(LoginView):
    template_name = 'DesignPro/login.html'


class BBLogoutView(LogoutView):
    template_name = 'DesignPro/logged_out.html'


from .forms import RegisterUserForm


class RegisterView(CreateView):
    template_name = 'DesignPro/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
