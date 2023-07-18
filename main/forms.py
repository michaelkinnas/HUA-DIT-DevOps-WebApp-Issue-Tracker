from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class createNewIssue(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    description = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))    
    TYPE = [
        ("B", "Bug"),
        ("F", "Feature"),
        ("T", "Task"),
    ]
    type = forms.CharField(label='Type', widget = forms.Select(choices=TYPE, attrs={'class':'form-select'}))
    
class createNewProject(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    description = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))