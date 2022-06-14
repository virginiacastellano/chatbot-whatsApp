import pyautogui, webbrowser 
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone= +54 "numero de telefono")
sleep(30)


#aca podemos adaptar el mensaje seugun su nombre, en este caso es "spam.tet" si deo usar el de delitos, colocaremos "delitos_2020.csv" y asi podemos adaptarlo a cualquier archivo 
with open ("spam.txt", "r") as columns:
    for line in columns:
       pyautogui.typewrite(line)
       pyautogui.press("enter")



##esto sirve solo para  texto 
# webbrowser.open("https://web.whatsapp.com/send?phone=")
# sleep(10)

# pyautogui.typewrite("Hola estoy es un mensaje automatico")
# pyautogui.press("enter")

# import pyautogui, webbrowser
# from time import sleep