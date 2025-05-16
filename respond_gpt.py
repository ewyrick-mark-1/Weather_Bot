import json
import requests
import wandb
from openai import OpenAI
TOKEN = 'ENTER TOKEN HERE'
client = OpenAI(api_key=TOKEN)
system_message = """
## Today's Weather Summary

- **Date**: {date}
- **Location**: {location}

## Temperature Details
- **High**: {temp_high}°F
- **Low**: {temp_low}°F
- **Current Temperature**: {temp_current}°F

## Wind Conditions
- **Speed**: {wind_speed} mph
- **Direction**: {wind_direction}

## Precipitation Forecast
- **Chance of Rain**: {rain_chance}%
- **Rainfall Amount**: {rain_amount} inches

## Additional Observations
- **Humidity**: {humidity}%
- **Visibility**: {visibility} miles
- **Sunrise/Sunset**: {sunrise} / {sunset}

## Summary
{summary}
"""


def handle_response():
 info = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Indianapolis&appid=1b4922de6ec620de5d2aeacaf2bee3c5&units=imperial').text

 completion = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": info}
  ]
 )
 newbie = completion.choices[0].message.content
 return newbie