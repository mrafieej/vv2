from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    location = forms.CharField(required=False)
    occupation = forms.CharField(required=False)
    about = forms.CharField(widget=forms.Textarea, required=False)
    required_css_class = 'required'

    class Meta:
        model = UserProfile
        fields = ['email', 'firstname', 'lastname', 'location', 'occupation', 'about', 'profile_pic', 'password']
        labels = {
            "firstname": "First Name",
            "lastname": "Last Name",
            "profile_pic": "Profile Pic.",
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )