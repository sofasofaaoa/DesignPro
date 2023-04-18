from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .models import Request, Category


def index(request):
    in_progress = Request.objects.all().filter(status='i').count()
    done = Request.objects.filter(status='c')

    return render(request, 'index.html', context={'in_progress': in_progress,
                                                  'done': done})


@permission_required('user.is_superuser')
class RequestListView(ListView):
    model = Request


class RequestDetailView(DetailView):
    model = Request


@permission_required('user.is_superuser')
class CategoryListView(ListView):
    model = Category


class BBLoginView(LoginView):
    template_name = 'DesignPro/login.html'


class BBLogoutView(LogoutView):
    template_name = 'DesignPro/logged_out.html'


from .forms import RegisterUserForm


class RegisterView(CreateView):
    template_name = 'DesignPro/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class CreateRequest(LoginRequiredMixin, CreateView):
    model = Request
    fields = '__all__'


class DeleteRequest(LoginRequiredMixin, DeleteView):
    model = Request
    success_url = reverse_lazy('profile')


@permission_required('user.is_superuser')
class UpdateRequest(UpdateView):
    model = Request
    fields = ['status', 'photo', 'comm']


@permission_required('user.is_superuser')
class CreateCategory(CreateView):
    model = Category
    fields = '__all__'


@permission_required('user.is_superuser')
class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
