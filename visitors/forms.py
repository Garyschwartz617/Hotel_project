from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Booking, Contact
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','city','number']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['people','book_start','book_end']   

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         # fields =[' __all__']
#         fields = ['message', 'staff_members']
