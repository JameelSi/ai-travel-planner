from django import forms

class TravelPlanForm(forms.Form):
    destination = forms.CharField(label="Destination", max_length=100)
    start_date = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type': 'date'}))
    budget = forms.DecimalField(label="Budget ($)", max_digits=10, decimal_places=2)
    style = forms.ChoiceField(label="Travel Style", choices=[
        ('adventure', 'Adventure'),
        ('luxury', 'Luxury'),
        ('food', 'Food'),
        ('culture', 'Culture'),
        ('nature', 'Nature'),
    ])
