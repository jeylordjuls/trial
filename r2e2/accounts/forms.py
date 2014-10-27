from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Faculty, Organization, Guest, BuildingAdmin, DepartmentChair
from django.contrib import admin

class CustomUserCreationForm(UserCreationForm):
 
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = User

 
class FacultyUserCreationForm(UserCreationForm):

    additionalProperties = forms.CharField(label="Additional Properties", max_length=30, required=False,
        help_text="150 characters or fewer.")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
    class Meta:
        exclude =[]
        model = Faculty
 

class OrganizationUserCreationForm(UserCreationForm):

    additionalProperties = forms.CharField(label="Additional Properties", max_length=30, required=False,
        help_text="150 characters or fewer.")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
    class Meta:
        exclude =[]
        model = Organization

class GuestUserCreationForm(UserCreationForm):

    additionalProperties = forms.CharField(label="Additional Properties", max_length=30, required=False,
        help_text="150 characters or fewer.")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
    class Meta:
        exclude =[]
        model = Guest

class BldgAdminUserCreationForm(UserCreationForm):

    additionalProperties = forms.CharField(label="Additional Properties", max_length=30, required=False,
        help_text="150 characters or fewer.")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
    class Meta:
        exclude =[]
        model = BuildingAdmin

class DepartmentChairUserCreationForm(UserCreationForm):

    additionalProperties = forms.CharField(label="Additional Properties", max_length=30, required=False,
        help_text="150 characters or fewer.")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 
    class Meta:
        exclude =[]
        model = Guest
