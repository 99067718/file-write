import tkinter as tk
import pygame

pygame.mixer.init()

def Play(soundname = ""):
    pygame.mixer.music.load(f'Assets\Audio\{soundname}')
    pygame.mixer.music.play(loops=0)
window = tk.Tk()
window.title("ScreenLock")
window.configure(bg="yellow")
window.geometry("800x500")
window.attributes('-fullscreen', True)
OnOff = "on"
lightOn = tk.PhotoImage(file='Assets\Images\On.png')
lightOff = tk.PhotoImage(file='Assets\Images\Off.png') 
window.wm_attributes('-transparentcolor', 'yellow')


def Click():
    global OnOff
    if OnOff == "off":
        button.configure(image= lightOn)
        window.configure(bg="yellow")
        OnOff = "on"
        file = open("actions.log", "a")
        file.write("\nLight has been turned on")
        file.close()


    else:
        window.configure(bg="black")
        OnOff = "off"
        button.configure(image= lightOff)
        file = open("actions.log", "a")
        file.write("\nLight has been turned off")
        file.close()

button = tk.Button(image= lightOn, bg="white", fg="black",command = Click, borderwidth=0)
button.pack(pady = 30, padx = 30)

window.mainloop()