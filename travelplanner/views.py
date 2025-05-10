from django.shortcuts import render
from .forms import TravelPlanForm
from .itinerary_engine import generate_itinerary

def plan_trip(request):
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            data = form.cleaned_data
            itinerary = generate_itinerary(data)  # Send the data to OpenAI
            
            # Pass the form data and the itinerary to the template
            context = {
                'form': form,
                'itinerary': itinerary,
            }
            return render(request, 'form.html', context)
    else:
        form = TravelPlanForm()

    return render(request, 'form.html', {'form': form})
