import requests

from tkinter import messagebox

API_KEY = 'a901017cfbb05f0669ecc5b5509f6a48'
def get_weather(city_entry, result_city, result_temp, result_humidity, result_desc):
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        result_city.config(text=f"City: {city.title()}")
        result_temp.config(text=f"Temperature: {temperature} °C")
        result_humidity.config(text=f"Humidity: {humidity}%")
        result_desc.config(text=f"Description: {description.title()}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get data: {e}")



