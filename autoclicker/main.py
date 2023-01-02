from time import sleep
import keyboard
import mouse
from tkinter import *

def Autoclicker():

    start_key = "o"

    stop_key = "p"

    while True:
        if keyboard.is_pressed(start_key):
            mouse.is_pressed(button = 'left')
            while True:
                sleep(0.01)
                mouse.double_click(button = 'left')
                if keyboard.is_pressed(stop_key):
                    break


Autoclicker()
