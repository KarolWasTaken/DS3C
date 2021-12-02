import tkinter as tk
import variables
from tkinter import *

class InfoBoxClass(object):
    def infoBox(event):
        infoRoot = Tk()
        infoRoot.title("Welcome!")                                    
        infoRoot.iconbitmap(variables.resource_path("iconds3.ico"))
        infoCanvas = tk.Canvas(infoRoot, width = 500, height = 500)  # window to say data has been reset to default.
        infoCanvas.pack()  
        labelTitle = tk.Label(infoRoot, text= "Welcome to DS3C!", font=("Yu Gothic", 30))    # Courier Century Gothic
        labelSubtitle = tk.Label(infoRoot, text= "How To Use DS3C", font=("Franklin Gothic Book", 15, "bold"))
        labelText = tk.Label(infoRoot, text= "This is a pretty simple program to use. When the counter has loaded in, press 'y' \
on your keyboard to bring up the options menu. In there you'll be able to edit the number of deaths, font, font and \
background colour, and savedata location; aswell as reset the settings back to default and, most importantly, connect your \
game to Dark Douls 3!", font=("Century Gothic", 10), wraplength=450)
        labelSubtitle2 = tk.Label(infoRoot, text= "WARNING", font=("Franklin Gothic Book", 15, "bold"), fg="red")
        labelText2 = tk.Label(infoRoot, text= "I don't THINK this program can ban a player BUT I could be wrong. It doesn't attach itself \
to the game - or attach any kind of debugger to it either. It simply reads the current health value of the player in a similar way that \
Cheat Engine does. Always exercise caution when it comes to things like this. To stay extra safe you could:", font=("Century Gothic", 10), wraplength=450)
        labelBullet = tk.Label(infoRoot, text= "\u2022 Turn your steam to offline mode \n\u2022 Turn your Dark Souls into offline mode \n\u2022 Make a second \
steam account and family share Dark Souls 3 to it ", font=("Century Gothic", 10), wraplength=450, anchor="w", justify=LEFT)
        labelText3 = tk.Label(infoRoot, text= "To see this menu again press 'i' on the deathcount.", font=("Century Gothic", 10))

        infoCanvas.create_window(250, 50, window=labelTitle)
        infoCanvas.create_window(250, 100, window=labelSubtitle)
        infoCanvas.create_window(250, 170, window=labelText)
        infoCanvas.create_window(250, 240, window=labelSubtitle2)
        infoCanvas.create_window(250, 300, window=labelText2)
        infoCanvas.create_window(250, 375, window=labelBullet)
        infoCanvas.create_window(250, 470, window=labelText3)
        infoCanvas.create_rectangle(450, 102.5, 60, 98.5, fill='black')  #x1 y1 x2 y2
        infoCanvas.create_rectangle(450, 242.5, 60, 238.5, fill='black')
        infoRoot.mainloop()   