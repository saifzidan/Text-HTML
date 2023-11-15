from django import forms
from ckeditor.widgets import CKEditorWidget
class Field(forms.Form):
    content = forms.CharField(widget=CKEditorWidget() , label='')