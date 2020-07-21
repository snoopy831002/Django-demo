from django import forms
from .models import Tag

class create_articles_form(forms.Form):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': "form-control"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.SelectMultiple(attrs={'class': "selectpicker"}))


