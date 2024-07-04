from django import forms
from .models import Reservation

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
