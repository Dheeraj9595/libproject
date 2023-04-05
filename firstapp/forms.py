from django import forms
from .models import Book

class BookForm(forms.ModelForm): #built in model form
    class Meta:
        model = Book
        fields = "__all__"
# fields = "__all__"
# exclude = ("is_active",)  #for excluding is active checkbox
# exclude = ("author",) #for excluding is Author field


# class BookForm(forms.Form): #forms.form is user define form

#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     roll_number = forms.IntegerField(help_text= "Enter 6 digit roll number")
#     password = forms.CharField(widget= forms.PasswordInput())


# print(BookForm())


# --------------------------------------django forms-------------------------------------------------------------

from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
