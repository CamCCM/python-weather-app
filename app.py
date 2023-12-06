import requests
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

api_key = "886df1aa80ab8cc5bb60b3c1d09abbca"

def get_weather():
    city = text_field.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    weather = requests.get(url).json()

    if weather["cod"] == 200:
        description = weather["weather"][0]["main"]
        temp = round(weather["main"]["temp"])
        pressure = weather["main"]["pressure"]
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]

        temp_label.config(text=f"{temp}° F")
        desc_text.config(text=description)
        pressure_text.config(text=pressure)
        humidity_text.config(text=f"{humidity}%")
        wind_text.config(text=f"{wind} mph")
    else:
        temp_label.config(text="Please enter a valid city")
        desc_text.config(text="...")
        pressure_text.config(text="...")
        humidity_text.config(text="...")
        wind_text.config(text="...")
    

city_label = Label(text="City:", font=("poppins", 10, "bold")).place(x=15,y=40)

text_field = Entry(window, justify="center", width=17, font=("poppins", 10))
text_field.place(x=50, y=40)
text_field.focus()

search_button = Button(text="Search", cursor="hand2", width=8, command=get_weather).place(x=180, y=39)

weather_label = Label(text="Weather", font=("poppins", 30, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)

# time_label = Label(text="", font=("poppins", 15))
# time_label.place(relx=0.5, rely=0.28, anchor=CENTER)

temp_label = Label(text="", font=("poppins", 40, "bold"))
temp_label.place(relx=0.5, rely=0.45, anchor=CENTER)

desc_label = Label(text="Description", font=("poppins", 15, "bold"))
desc_label.place(relx=0.20, rely=0.8, anchor=CENTER)
wind_label = Label(text="Wind", font=("poppins", 15, "bold"))
wind_label.place(relx=0.40, rely=0.8, anchor=CENTER)
humidity_label = Label(text="Humidity", font=("poppins", 15, "bold"))
humidity_label.place(relx=0.60, rely=0.8, anchor=CENTER)
pressure_label = Label(text="Pressure", font=("poppins", 15, "bold"))
pressure_label.place(relx=0.80, rely=0.8, anchor=CENTER)

desc_text = Label(text="...", font=("poppins", 13))
desc_text.place(relx=0.20, rely=0.85, anchor=CENTER)
wind_text = Label(text="...", font=("poppins", 13))
wind_text.place(relx=0.40, rely=0.85, anchor=CENTER)
humidity_text = Label(text="...", font=("poppins", 13))
humidity_text.place(relx=0.60, rely=0.85, anchor=CENTER)
pressure_text = Label(text="...", font=("poppins", 13))
pressure_text.place(relx=0.80, rely=0.85, anchor=CENTER)

mainloop()