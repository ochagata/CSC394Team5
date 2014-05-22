from django import forms
from ARK.models import PazzosUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PazzosProfileForm(forms.ModelForm):
    
    class Meta:
        model = PazzosUser
        fields = ('gender', 'age', 'handedness', 'english_level')

class PazzosRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True, max_length = 10)
    last_name = forms.CharField(required = True, max_length = 10)
    class Meta:
        model = User
        fields = ('email','password1','password2')

    def save(self, commit=True):
        user = super(PazzosRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            
        return user
