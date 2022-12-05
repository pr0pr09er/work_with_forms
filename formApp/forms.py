from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(empty_value='имя')
    surname = forms.CharField(empty_value='фамилия')
    email = forms.CharField(empty_value='почта')
    country = forms.CharField(empty_value='страна')
    city = forms.CharField(empty_value='город')
    street = forms.CharField(empty_value='улица')
    number_of_house = forms.IntegerField()
    flat = forms.IntegerField()
