# travelplanner/itinerary_engine.py
import openai

def generate_itinerary(data):
    # Set up OpenAI API key (make sure to set your API key in an environment variable)
    openai.api_key = "your_openai_api_key"

    prompt = f"Create a travel itinerary for {data['destination']} from {data['start_date']} to {data['end_date']} with a budget of ${data['budget']} and a {data['style']} style."

    response = openai.Completion.create(
        engine="text-davinci-003",  # Or another model
        prompt=prompt,
        max_tokens=500
    )

    # Parse the response
    itinerary = response.choices[0].text.strip().split("\n")
    itinerary_data = [{'date': day.split(":")[0], 'details': day.split(":")[1]} for day in itinerary]

    return itinerary_data
