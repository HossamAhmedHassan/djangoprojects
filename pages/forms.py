from django import forms
from .models import Restaurant,Product

class RestaurantCreate(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = Restaurant
        fields = '__all__'


class ProductCreate(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = Product
        fields = '__all__'
        
