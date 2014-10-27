from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
 
from .models import CustomUser, Faculty, Organization, Guest, BuildingAdmin, DepartmentChair, Adviser
from .forms import CustomUserCreationForm, FacultyUserCreationForm, OrganizationUserCreationForm, GuestUserCreationForm, BldgAdminUserCreationForm, DepartmentChairUserCreationForm
 
class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
 
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Adviser)
 
class FacultyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'priorityLevel', 'additionalProperties')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'additionalProperties')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = FacultyUserCreationForm
 
admin.site.register(Faculty, FacultyUserAdmin)
 
class OrganizationUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'priorityLevel', 'additionalProperties')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'additionalProperties')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = OrganizationUserCreationForm
 
admin.site.register(Organization, OrganizationUserAdmin)

class GuestUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'priorityLevel', 'additionalProperties')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'additionalProperties')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = GuestUserCreationForm
 
admin.site.register(Guest, GuestUserAdmin)

class BuildingAdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'priorityLevel', 'additionalProperties')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'additionalProperties')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = BldgAdminUserCreationForm
 
admin.site.register(BuildingAdmin, BuildingAdminUserAdmin)

class DepartmentChairUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'priorityLevel', 'additionalProperties')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'additionalProperties')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = DepartmentChairUserCreationForm
 
admin.site.register(DepartmentChair, DepartmentChairUserAdmin)