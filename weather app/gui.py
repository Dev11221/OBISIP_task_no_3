import tkinter as tk
from weatherapp import get_weather
import requests
# Define your OpenWeatherMap API key here
API_KEY = 'a901017cfbb05f0669ecc5b5509f6a48'

def fetch_city_suggestions(query):
    try:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        suggestions = []
        for item in data:
            city = item['name']
            country = item.get('country', '')
            state = item.get('state', '')
            if state:
                suggestions.append(f"{city}, {state}, {country}")
            else:
                suggestions.append(f"{city}, {country}")
        return suggestions
    except:
        return []

def update_suggestions(entry_text, listbox):
    input_text = entry_text.get()
    listbox.delete(0, tk.END)
    if input_text:
        suggestions = fetch_city_suggestions(input_text)
        for city in suggestions:
            listbox.insert(tk.END, city)

def on_city_select(event, city_entry, listbox):
    try:
        selection = listbox.get(listbox.curselection())
        city_entry.delete(0, tk.END)
        city_entry.insert(0, selection)
        listbox.delete(0, tk.END)
    except:
        pass

def create_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("400x400")
    root.config(bg="lightblue")
    root.resizable(False, False)

    tk.Label(root, text="Enter City Name", font=("Arial", 14), bg="lightblue").pack(pady=10)

    city_entry = tk.Entry(root, font=("Arial", 14), width=25)
    city_entry.pack()

    suggestion_box = tk.Listbox(root, font=("Arial", 12), height=5)
    suggestion_box.pack(pady=2)

    result_city = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
    result_temp = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
    result_humidity = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
    result_desc = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")

    city_entry.bind("<KeyRelease>", lambda e: update_suggestions(city_entry, suggestion_box))
    suggestion_box.bind("<<ListboxSelect>>", lambda e: on_city_select(e, city_entry, suggestion_box))

    tk.Button(
        root,
        text="Get Weather",
        font=("Arial", 12, "bold"),
        bg="skyblue",
        command=lambda: get_weather(city_entry, result_city, result_temp, result_humidity, result_desc)
    ).pack(pady=10)

    result_city.pack(pady=5)
    result_temp.pack(pady=5)
    result_humidity.pack(pady=5)
    result_desc.pack(pady=5)

    root.mainloop()