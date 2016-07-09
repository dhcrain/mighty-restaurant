from django import forms
from mighty_app.models import Order, MenuItem, OrderLine, Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['job']
