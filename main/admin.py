from django.contrib import admin

from .models import User, FileSet, Temporary
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_paid')
    list_filter = ('is_paid', ('date_joined'),)
    search_fields = ['username']


class FileSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ['name']


class TemporaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(FileSet, FileSetAdmin)
admin.site.register(Temporary, TemporaryAdmin)
