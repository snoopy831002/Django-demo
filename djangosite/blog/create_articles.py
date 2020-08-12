from django import forms
from .models import Tag, Articles

class edit_articles_form(forms.Form):
    def __init__(self,id):
        super(edit_articles_form, self).__init__()
        self.fields['title'].initial = Articles.objects.filter(id=id)[0].title
        self.fields['content'].initial = Articles.objects.filter(id=id)[0].content
        self.fields['tags'].initial = Articles.objects.filter(id=id)[0].tags.all()
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': "form-control"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.SelectMultiple(attrs={'class': "selectpicker"}))

class create_articles_form(forms.Form):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': "form-control"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.SelectMultiple(attrs={'class': "selectpicker"}))