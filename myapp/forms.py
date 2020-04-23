from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Item

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ItemForm(forms.ModelForm):
    # detail1 = forms.CharField(max_length=20)
    # detail2 = forms.CharField(max_length=20)
    # detail3 = forms.CharField(max_length=20)
    # material = forms.CharField(max_length=20)
    # gauge = forms.CharField(max_length=10)
    # quantity = forms.CharField(max_length=10)
    # rate = forms.CharField(max_length=10)
    # size = forms.CharField(max_length=20)
    # colour = forms.CharField(max_length=20)
    # podetail = forms.CharField(max_length=40)
    # process = forms.CharField(max_length=40)
    # billdetail = forms.CharField(max_length=40)
    # stock = forms.CharField(max_length=20)
    class Meta:
        model=Item
        fields = [
            'id','detail1','detail2','detail3',
            'material','gauge','quantity',	'rate',	'size',	
            'colour','podetail','process','billdetail','stock'
        ]