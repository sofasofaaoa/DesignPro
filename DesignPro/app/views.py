from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
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

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Request.objects.all()
        else:
            return Request.objects.filter(user=self.request.user)


class CategoryListView(PermissionRequiredMixin, ListView):
    model = Category
    permission_required = 'user.is_superuser'
    template_name = 'DesignPro/category_list.html'


class BBLoginView(LoginView):
    template_name = 'DesignPro/login.html'


class BBLogoutView(LogoutView):
    template_name = 'DesignPro/logged_out.html'


from .forms import RegisterUserForm, AddDesignRequest, AddCommentRequest


class RegisterView(CreateView):
    template_name = 'DesignPro/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class CreateRequest(LoginRequiredMixin, CreateView):
    model = Request
    fields = ['user', 'title', 'summary', 'category']
    success_url = reverse_lazy('requests')
    template_name = 'DesignPro/request_form.html'


class DeleteRequest(LoginRequiredMixin, DeleteView):
    model = Request
    success_url = reverse_lazy('requests')
    template_name = 'DesignPro/request_confirm_delete.html'


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


@permission_required('user.is_superuser')
def confirm_update(request, pk, st):
    newrequest = Request.objects.get(id=pk)
    newrequest.save()

    if st == 'c':
        if request.method == 'POST':
            form = AddDesignRequest(request.POST, request.FILES)
            if form.is_valid():
                newrequest.design = form.cleaned_data['design']
                newrequest.status = st
                newrequest.save()
                return redirect('requests')
        else:
            form = AddDesignRequest()
        return render(request, 'DesignPro/request_form.html', {'form': form})

    if st == 'i':
        if request.method == 'POST':
            form = AddCommentRequest(request.POST, request.FILES)
            if form.is_valid():
                newrequest.comment = form.cleaned_data['comm']
                newrequest.status = st
                newrequest.save()
                return redirect('requests')
        else:
            form = AddCommentRequest()
        return render(request, 'DesignPro/request_form.html', {'form': form})
