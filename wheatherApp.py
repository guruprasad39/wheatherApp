
from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "71a1ceda81264e656273bfd172e6f9d1"  # Replace with your actual API key

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Weather App</title>
            <link rel="stylesheet" type="text/css" href="static/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Weather Finder</h1>
                <form action="/weather" method="get">
                    <label for="city">Enter city:</label>
                    <input type="text" name="city" id="city" placeholder="Enter city name" required>
                    <input type="submit" value="Get Weather">
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return "Please provide a city name!"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f'''
        <html>
            <head>
                <title>Weather in {city}</title>
                <link rel="stylesheet" type="text/css" href="static/styles.css">
            </head>
            <body>
                <div class="container">
                    <h1>Weather in {city}</h1>
                    <p>Temperature: {temp}°C</p>
                    <p>Description: {desc}</p>
                    <a href="/">Back to Home</a>
                </div>
            </body>
        </html>
        '''
    else:
        return f"Could not fetch weather for {city}. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
