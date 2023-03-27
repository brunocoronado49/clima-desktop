from tkinter import *
import requests


def clima(ciudad):
    try:
        API_KEY = "7a9a10b94cfc0dc055634f971248f593"
        API_URL = "https://api.openweathermap.org/data/2.5/weather"
        
        params = {"APPID": API_KEY, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(API_URL, params=params)
        clima = response.json()
        print(clima["name"])
        print(clima["weather"][0]["description"])
        print(clima["main"]["temp"])
    except:
        print("Error")
    
    show_response(clima)
    
def show_response(clima):
    try:
        name = clima["name"]
        description = clima["weather"][0]["description"]
        tep = clima["main"]["temp"]
        
        city["text"] = name
        temp["text"] = str(int(tep)) + "º C"
        desc["text"] = description
    except:
        city["text"] = "Ingresa un nombre valido"


ventana = Tk()
ventana.title("Clima app")
ventana.geometry("350x550")

texto = Entry(ventana, font=("Courier", 20, "normal"), justify="center")
texto.pack(padx=30, pady=30)

get_clima = Button(ventana, text="Consulta el clima", font=("Courier", 20, "normal"), command= lambda: clima(texto.get()))
get_clima.pack()

city = Label(font=("Courier", 20, "normal"))
city.pack(padx=20, pady=20)

temp = Label(font=("Courier", 50, "normal"))
temp.pack(padx=10, pady=10)

desc = Label(font=("Courier", 20, "normal"))
desc.pack(padx=10, pady=10)

ventana.mainloop()