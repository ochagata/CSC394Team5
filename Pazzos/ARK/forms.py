from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from ARK.models import PazzosUser, PazzosTest, PazzosTestWord
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
       # flag = self.cleaned_data['is_staff']
        pdb.set_trace()
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
        fields = ('email','password','first_name','last_name','is_active','gender','handedness','age')

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit = True):
        user = super(PazzosChangeForm, self).save(commit = False)
        user.is_superuser = self.cleaned_data['is_staff']
        if commit:
            user.save()
        return user

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

class PazzosWordForm(forms.ModelForm):
    word = forms.CharField(max_length = 255)

    class meta:
        model = PazzosTestWord
        fields = ('word',)

    def save(self, commit = True):
        #pdb.set_trace()
        word = super(PazzosWordForm, self).save(commit = False)
        word.wordLength = len(word.word)
        if word:
            word.save()
        return word

class PazzosTestForm(forms.ModelForm):
    class Meta:
        model = PazzosTest
        fields = ('takenBy','word_list', 'correct_list', 'timeStarted', 'timeCompleted' )

    def clean(self):
        correct = self.cleaned_data.get('correct_list')
        total = self.cleaned_data.get('word_list')
        correctSet = set(list(correct))
        totalSet = set(list(total))
        if len(correct) > len(total):
            raise ValidationError("The list of correct words is bigger than the list of words in the test!")
        if not set(list(correct)).issubset(set(list(total))):
            raise ValidationError("The list of correct words contains words that aren't in the test!")
        return self.cleaned_data