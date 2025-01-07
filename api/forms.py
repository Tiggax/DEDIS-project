from api import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from api.models import ClimbUser

class ClimbUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    class Meta(UserCreationForm.Meta):
        model = ClimbUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
            


class ClimbUserUpdateForm(UserChangeForm):
    pass