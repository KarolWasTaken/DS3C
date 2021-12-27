import tkinter as tk
import random as rand
import variables, json, process_interface
from tkinter import *
from tkinter import colorchooser, messagebox, filedialog, ttk
from time import sleep


def setflag(event): # flag to make sure options menu is only opened once.
    variables.ontop = False 

def setflag2(event):
    variables.ontop2 = False


class Options(object):

    def optionsMenu(event):                                                                            
        try:

            if not variables.ontop:
                root = tk.Toplevel()             # make sure options is only open once
                root.bind('<Destroy>', setflag)    
            variables.ontop = True

            root.bind("<i>", variables.info.infoBox)  # info box
            root.bind("<I>", variables.info.infoBox)

            variables.firstclick = True # resets first click for reopening the options menu (death input ghost text)

            root.iconbitmap(variables.resource_path("iconds3.ico"))
            root.title("Options")                                                   # standard stuff. Setup etc.
            

            canvas1 = tk.Canvas(root, width = 300, height = 350)               # for the sake of this looking clean ill use the Canvas method
            canvas1.pack()                                                        #^ so i dont have to pack stuff over and over.
            entry = Entry(root, width = 30, bd =1)    

            def clicked():
                try:                                                             # try: to catch an incorrect data type error                          
                    x1 = int(entry.get())                          # checks what was inputted
                    if(isinstance(x1, int) == True):               # looks if its an int or not
                        variables.actualData = x1                            # updates actualData to be number entered
                        myLabel = Label(root, text = "                  Done! Now close this window.                  ")                                  
                        canvas1.create_window(150, 320, window=myLabel)          # make text for when button is clicked && instantiate the text
                except:       # catches exception (incorrect data type)
                    myLabel = Label(root, text = "                That data wasnt a number. Try again.                ")
                    canvas1.create_window(150, 320, window=myLabel)                   # error text
            def fontChange(event):
                try:
                    
                    x2 = myComboFont.get()   # grabs font selectd from list
                    variables.txtFont = x2  #sets it to that font
                    fcLabel = Label(root, text= "                      Done! Font has now been changed.                      ")
                    canvas1.create_window(150, 320, window=fcLabel)
                except:
                    fcLabel = Label(root, text= "Something went wrong. Is the name correct?")  # incase something, somehow, goes wrong here.
                    canvas1.create_window(150, 320, window=fcLabel)
            def chooseColourFont():
                ogColourF = variables.colourCodeFont # guard against inputting nothing
                # variable to store hexadecimal code of color
                variables.colourCodeFont = colorchooser.askcolor(title ="Choose colour")[1]     #i dont care if this isnt efficient
                if(variables.colourCodeFont == None):
                    variables.colourCodeFont = ogColourF
                else:    
                    variables.jsonData['font colour'] = variables.colourCodeFont
            def chooseColourBack():
                ogColourG = variables.colourCodeBack # guard against inputting nothing
                variables.colourCodeBack = colorchooser.askcolor(title ="Choose colour")[1]
                if(variables.colourCodeBack == None):
                    variables.colourCodeBack = ogColourG
                else:
                    variables.jsonData['background colour'] = variables.colourCodeBack
            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.destroy()
            def on_entry_click(event):
                #function that gets called whenever entry1 is clicked        

                if variables.firstclick: # if this is the first time they clicked it
                    variables.firstclick = False
                    entry.delete(0, "end") # delete all the text in the entry
            def resetSettings():
                # resets all settings to default.
                windowNames = ["Just like that!", "Magic.", "Viola!", "Aaaaaaaaaaand now it's boring.",
                "Old gold.", "Good old", "Nothing beats home", "Bored of ruining perfection?",":0...?",  # just a cute little feature
                "Missclick...?", "Perfections at last!"]

                variables.actualData = 0
                variables.colourCodeFont = "white"
                variables.colourCodeBack = "green"
                variables.txtFont = "Comic Sans MS"
                resetRoot = Tk()
                resetRoot.title(rand.choice(windowNames))                                    
                resetRoot.iconbitmap(variables.resource_path("iconds3.ico"))
                resetCanvas = tk.Canvas(resetRoot, width = 340, height = 100)  
                resetCanvas.pack()  
                labelreset = tk.Label(resetRoot, text= "Settings have been reset to default!")   
                resetCanvas.create_window(170, 50, window=labelreset)
                resetRoot.mainloop()
                variables.JSON.writeToJSONFile(variables.path, variables.fileName, variables.jsonData)
            def selectPath():
                ogPath = variables.path                # to remember selected path before user changed it.

                variables.path = filedialog.askdirectory()        # if the user opens and then closes the app, it'll set 'path' to be empty.
                if (variables.path == ""):                        # this guards agaisnt that
                    variables.path = ogPath
                else:
                    with open(variables.sendToDir + "/DS3C/path.json", 'w+') as fp:
                        json.dump(variables.path, fp)
            def connectDS3():
                try:
                    if (variables.ontop2 == False):
                        root = tk.Toplevel()             # make sure this option is only open once
                        root.bind('<Destroy>', setflag2)    
                    variables.ontop2 = True
                    root.iconbitmap(variables.resource_path("iconds3.ico"))
                    
                    variables.process.open(name = 'DarkSoulsIII')
                    sleep(1.5)
                    if(process_interface.canReadAddress):
                        
                        root.title("Connected to DS3!")
                        DS3Canv = tk.Canvas(root, width = 340, height = 100)       
                        DS3Canv.pack()
                        labelDS3 = tk.Label(root, text= "Successfully connected to your game window!\n You can close this window now.")
                        DS3Canv.create_window(170, 50, window=labelDS3)
                        variables.connectedToGame = False
                        root.mainloop()
                    else:
                        raise ValueError('A very specific bad thing happened.')
                except:
                    root.title("Something went wrong.")
                    DS3Canv = tk.Canvas(root, width = 340, height = 100)       
                    DS3Canv.pack()
                    labelDS3 = tk.Label(root, text= "Couldn't connect to Dark Souls 3\n Are you in-game?")
                    DS3Canv.create_window(170, 50, window=labelDS3)
                    root.mainloop()

            entry.insert(0, 'Enter your deaths...')
            entry.bind('<FocusIn>', on_entry_click)                                                                                    
            canvas1.create_window(150, 30, window=entry)   # input box creation && instantiate the input box

            fontText = Label(root, text = "Change font:")      
            canvas1.create_window(40, 235, window=fontText)         # change font text

            myButtonDeaths = Button(root, text = "Enter deaths", command = clicked)                            
            canvas1.create_window(150, 70, window=myButtonDeaths)           # (death) button creation && instantiate the button    

            myButtonFontColour = Button(root, text = "Change font colour", command = chooseColourFont)
            canvas1.create_window(70, 110, window=myButtonFontColour) # font colout

            myButtonBgColour = Button(root, text = "Change background colour", command = chooseColourBack)
            canvas1.create_window(210, 110, window=myButtonBgColour) # background colour

            myButtonDefault = Button(root, text = "Reset settings to default", command = resetSettings)
            canvas1.create_window(150, 150, window=myButtonDefault) # reset to default settings

            myButtonPath = Button(root, text = "Select Savedata directory", command = selectPath)
            canvas1.create_window(150, 190, window=myButtonPath) # path to save data

            myComboFont = ttk.Combobox(root, value = variables.fonts)
            myComboFont.current(0)                                   # font combobox
            myComboFont.bind("<<ComboboxSelected>>", fontChange)
            canvas1.create_window(150, 235, window=myComboFont)

            myButtonConnectDS3 = Button(root, text = "Connect to DS3", command = connectDS3)
            canvas1.create_window(150, 280, window=myButtonConnectDS3)

            root.protocol("WM_DELETE_WINDOW", on_closing)     # close window confirm stuff

            root.resizable(False, False) # stop window from being resized
            root.mainloop()
        except:
            pass
