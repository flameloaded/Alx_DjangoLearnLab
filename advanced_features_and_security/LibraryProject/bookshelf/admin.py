from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
from django.utils.translation import gettext_lazy as _


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    list_filter = ('author', 'publication_year')            # filters on the right
    search_fields = ('title', 'author')                     # search box fields


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'role')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Role'), {'fields': ('role',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('username',)



admin.site.register(CustomUser, CustomUserAdmin)
