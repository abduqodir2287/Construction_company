from django import forms
from .models import Contact

class Contacts_Forms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


