from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class DashboardForm(ModelForm):


    class Meta:
        model = profile
        fields = ('username','name', 'address', 'dob', 'phone','country','count' )



'''class TransacForm(models.Model):
    desc = forms.TextInput()
    date = forms.DateField()
    amount = forms.IntegerField()
    receiver = forms.TextInput()
    sender = forms.TextInput()
    class Meta:
        model = transaction
        fields = ('sender', 'receiver', 'date', 'desc','amount', )'''

class CartForm(ModelForm):

    class Meta:
        model = Cart
        fields = ('i1c','q1c','i2c','q2c','i3c','q3c','i4c','q4c','i5c','q5c','i6c','q6c')