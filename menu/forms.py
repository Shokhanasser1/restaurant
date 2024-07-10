from django import forms
from .models import Reservation, Dish, Order
from PIL import Image

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'persons_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Select time'}),
            'persons_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Persons'}),
        }
        
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.username


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'image', 'description']
        
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            img = Image.open(image)
            if img.width <= 330 or img.height <= 300:
                raise forms.ValidationError("Размер изображения должен быть 330x300 пикселей")
        return image
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)