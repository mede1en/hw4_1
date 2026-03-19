from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class CustomRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=20, initial='+996', required=True)
    age = forms.IntegerField(required=True)
    city = forms.CharField(max_length=100, required=True)
    position = forms.CharField(max_length=100, required=True)
    experience_years = forms.IntegerField(required=True)
    education = forms.CharField(max_length=100, required=True)
    skills = forms.CharField(widget=forms.Textarea, required=True)
    github = forms.URLField(required=True)
    linkedin = forms.URLField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'password1', 
            'password2',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'age',
            'city',
            'position',
            'experience_years',
            'education',
            'skills',
            'github',
            'linkedin',
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.full_name = self.cleaned_data.get('full_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.age = self.cleaned_data.get('age')
        user.city = self.cleaned_data.get('city')
        user.position = self.cleaned_data.get('position')
        user.experience_years = self.cleaned_data.get('experience_years')
        user.education = self.cleaned_data.get('education')
        user.skills = self.cleaned_data.get('skills')
        user.github = self.cleaned_data.get('github')
        user.linkedin = self.cleaned_data.get('linkedin')

        if commit:
            user.save()

        return user