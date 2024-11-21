from django.contrib import admin

# Register your models here.
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from .models import Book


# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year",)
    list_filter = ("publication_year",)
    search_fields = ("title", "author")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)   

# Register the Book model
admin.site.register(Book)

# Adding groups and permissions via Django Admin
def create_groups_and_permissions():
    # Create groups
    viewer_group, created = Group.objects.get_or_create(name='Viewers')
    editor_group, created = Group.objects.get_or_create(name='Editors')
    admin_group, created = Group.objects.get_or_create(name='Admins')

    # Assign permissions to groups
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    viewer_group.permissions.set([can_view])
    editor_group.permissions.set([can_view, can_create, can_edit])
    admin_group.permissions.set([can_view, can_create, can_edit, can_delete])

# Call this function manually or from a Django management command