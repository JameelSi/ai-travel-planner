# travelplanner/forms.py
from django import forms

class TravelForm(forms.Form):
    destination = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    budget = forms.IntegerField()
    style_choices = [
        ('relax', 'Relax'),
        ('adventure', 'Adventure'),
        ('culture', 'Culture'),
        ('food', 'Food'),
        ('party', 'Party')
    ]
    style = forms.ChoiceField(choices=style_choices)
