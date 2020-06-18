from django import forms

class django_form(forms.Form):
    content = forms.CharField(required=True)