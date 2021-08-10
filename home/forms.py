from .models import *
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'image_link', 'sku',
                  'name', 'sizes', 'price', 'description')

        widgets = {
            'category': forms.TextInput(attrs={'size': 50, 'class': 'form-control', 'placeholder': 'Enter product '
                                                                                                   'category'}),
            'name': forms.TextInput(attrs={'size': 50, 'class': 'form-control', 'placeholder': 'Enter product '
                                                                                               'name'}),
            'sku': forms.TextInput(attrs={'size': 50, 'class': 'form-control', 'placeholder': 'Enter product '
                                                                                              'Id'}),
            'sizes': forms.TextInput(attrs={'size': 50, 'class': 'form-control', 'placeholder': 'Enter available '
                                                                                                'sizes'}),
            'price': forms.TextInput(
                attrs={'size': 50, 'class': 'form-control', 'placeholder': 'Enter product price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product description'})
        }
