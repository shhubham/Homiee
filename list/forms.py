from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.detail
        fields=['title','body','slug','thumb']
