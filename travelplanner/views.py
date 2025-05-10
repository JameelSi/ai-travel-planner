# travelplanner/views.py
from django.shortcuts import render
from .forms import TravelForm
from .itinerary_engine import generate_itinerary  # We'll create this next

def plan_trip(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            itinerary = generate_itinerary(data)  # This function will generate the itinerary using OpenAI
            return render(request, 'itinerary.html', {'itinerary': itinerary})
    else:
        form = TravelForm()
    return render(request, 'form.html', {'form': form})
