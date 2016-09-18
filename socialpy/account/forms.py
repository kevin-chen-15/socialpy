from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from .models import Profile, Comment
from django.utils.translation import ugettext_lazy as _

#Information entered when logging in
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#Information entered when registering
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        #From User fields
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        '''Check if both password matches'''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

#Information entered when editing 
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'email': _('Email address'),
        }

#Information entered when updating picture
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

#Name displayed
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#Information entered when commenting in a profile
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

