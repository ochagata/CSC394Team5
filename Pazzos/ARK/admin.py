from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from ARK.models import PazzosUser

# Register your models here.

class PazzosCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = PazzosUser
        fields = ('email','first_name','last_name')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit = True):
        user = super(PazzosCreationForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
#TODO: split this up into admin version and front-end version
#the admin should be able to change passwords, but the front-end user shouldn't see that password hash field
class PazzosChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    #password = forms.CharField(label = 'Current Password', widget = forms.PasswordInput)
    
    #newPassword1 = forms.CharField(label = 'New Password',widget = forms.PasswordInput)
    #newPassword2 = forms.CharField(label = 'Confirm New Password', widget = forms.PasswordInput)
    
    class Meta:
        model = PazzosUser
        fields = ('email','password','first_name','last_name','is_active','is_admin','gender','handedness','age')
        
    def clean_password(self):
        return self.initial["password"]
    
    #def clean_newPassword2(self):
    #    newPassword1 = self.cleaned_data.get("newPassword1")
    #    newPassword2 = self.cleaned_data.get("newPassword2")
    #    if newPassword1:
    #        if not newPassword2:
    #            raise forms.ValidationError("You must confirm your new password!")
    #        if newPassword1 != newPassword2:
    #            raise forms.ValidationError("New passwords don't match!")
    #    elif newPassword2:
    #        raise forms.ValidationError("You must fill out both new password fields!")
    #    return newPassword2
    

class PazzosAdmin(UserAdmin):
    form = PazzosChangeForm
    add_form = PazzosCreationForm
    
    list_display = ('email','first_name','last_name','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('first_name','last_name','gender','handedness','age')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')})
    )
    
    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': ('email','first_name','last_name','password1','password2')}
        ),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    
admin.site.register(PazzosUser, PazzosAdmin)

admin.site.unregister(Group)
