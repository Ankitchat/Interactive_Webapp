from django import forms
from .models import UserInfo


class Userform(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ("FullName", "Email", "Zip")
