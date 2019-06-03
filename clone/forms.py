from django import forms
from .models import Image , Profile , User
from pyuploadcare.dj.forms import ImageField

class ImageForm(forms.ModelForm):  
    class Meta:
        model = Image
        fields = ("title","image","description","link","posted_by")

class ProfileForm(forms.Form):
    bio = forms.CharField(label = "Bio")
    pic = ImageField(label = "Pic")
