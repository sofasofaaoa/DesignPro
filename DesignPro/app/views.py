from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class RequestListView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'DesignPro/request_list.html'


class CategoryListView(PermissionRequiredMixin, ListView):
    model = Category
    permission_required = 'user.is_superuser'
    template_name = 'DesignPro/category_list.html'


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
    success_url = reverse_lazy('requests')
    template_name = 'DesignPro/request_form.html'


class DeleteRequest(PermissionRequiredMixin, DeleteView):
    model = Request
    success_url = reverse_lazy('requests')
    permission_required = 'user.is_superuser'
    template_name = 'DesignPro/request_confirm_delete.html'


class UpdateRequest(PermissionRequiredMixin, UpdateView):
    model = Request
    fields = ['status', 'photo', 'comm']
    permission_required = 'user.is_superuser'
    template_name = 'DesignPro/request_form.html'


class CreateCategory(PermissionRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    permission_required = 'user.is_superuser'

    success_url = reverse_lazy('categories')
    template_name = 'DesignPro/category_form.html'


class DeleteCategory(PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    permission_required = 'user.is_superuser'
    template_name = 'DesignPro/category_confirm_delete.html'
