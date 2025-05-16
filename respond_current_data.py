from datetime import datetime
import json
import requests
#today = datetime.datetime.today()
def handle_response():
    
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Indianapolis&appid=1b4922de6ec620de5d2aeacaf2bee3c5&units=imperial').text
    js_data = json.loads(data)
    temp_info = f"Date: {datetime.utcfromtimestamp(js_data['dt']).strftime('%Y-%m-%d %H:%M:%S')}\nWeather: {js_data['weather'][0]['description']}, High of {js_data['main']['temp_max']}, Low of {js_data['main']['temp_min']}"
    print(temp_info)
    return temp_info

