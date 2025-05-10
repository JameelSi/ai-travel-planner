# travelplanner/itinerary_engine.py
import openai
import os

def generate_itinerary(data):
    # Set the OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your API key is set as an environment variable
    prompt = f"Create a travel itinerary for {data['destination']} from {data['start_date']} to {data['end_date']} with a budget of ${data['budget']} and a {data['style']} style."
    client = openai.OpenAI()

    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )

    itinerary_text = response.output_text.strip()
    # Process the itinerary text into a structured format (e.g., list of dictionaries)
    itinerary_data = []
    # Assuming the generated itinerary text has the format of each day on a new line
    for line in itinerary_text.split("\n"):
        if ":" in line:
            day, details = line.split(":", 1)
            itinerary_data.append({'date': day.strip(), 'details': details.strip()})
    # Return the structured data (list of dictionaries)
    return itinerary_data