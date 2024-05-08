from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeather API key
API_KEY = '157f74a1b9ccdbd9c7fc0b7119b0a58c'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        # Construct the full API URL
        weather_url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(weather_url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found or invalid request'}

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
