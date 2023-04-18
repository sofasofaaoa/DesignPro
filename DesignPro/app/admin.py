from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)


@admin.register(Request)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'status', 'date_time')
    list_filter = ('date_time', 'status')


class RequestInline(admin.TabularInline):
    model = Request
    extra = 0


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    inlines = [RequestInline]
