# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:50:45 2023

@author: lorenzo
"""

from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import requests
import json


window = Tk()
window.title("FSX Weather App")

window.geometry("600x600")
window.resizable(False, False)

window_label = Label(window, text= "Welcome to the FSX Weather App addon! This app will provide all weather data needed for FSX.")
window_label.pack(ipadx=10, ipady=40)


entry = StringVar(window)

entry_label = Label(window, text = "Enter the zip code of your location in the text box bellow.")
entry_label.place(x= 145, y = 150)
entry_label.focus()


entry_box = Entry(window, textvariable=entry)
entry_box.place(x = 45, y = 180, width = 500, height = 80)
entry_box.focus()


def city_name():
    return entry.get()

def enter_clicked():
    API_Key = "cb771e45ac79a4e8e2205c0ce66ff633"

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="
    full_url = base_url + API_Key +  "&zip=" + city_name() +"&units=metric"
    weather_data = requests.get(full_url).json()
    print(weather_data)
    
    def cloudsdescrip(): 
        return(weather_data['weather'][0]['description'])
    
    def precipitation():
        precipitation = weather_data['main']['pressure']
        if precipitation > 1022.689:
            return("low.")
        elif precipitation >= 1009.144 or precipitation <= 1022.689:
            return("moderate.")
        else:
            return("high.")
    

   
    def visibility():
        return (weather_data['visibility']/ 1000)
    def wind_speeds():
        return round((weather_data['wind']['speed']*1.9),2)
    
    def wind_direction():    
        return (weather_data['wind']['deg'])

    msg = f"The clouds in your location are {cloudsdescrip()}.\nThe precipitation in your location is considered to be {precipitation()}\nThe visibility in your location is {visibility()} km.\nThe wind speed in your location is {wind_speeds()} knots.\nThe winds are travelling at a direction of {wind_direction()} degrees.\n"
    showinfo(
        title = "Weather Data",
        message = msg
    )
    

enter_button = Button(window, text = "Enter", command = enter_clicked, height = 3, width = 30, bg = 'grey', fg = 'black')
enter_button.place(x = 190, y = 350)
window.mainloop()
