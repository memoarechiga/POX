from django import forms
from .models import Order, Menu

class NewSaleForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'quantity', 'price', 'total')

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price')
