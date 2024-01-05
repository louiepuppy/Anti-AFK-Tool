import tkinter as tk
import random
import time
import pyautogui

def keyboardPress():
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
    key = random.choice(keys)
    if keyboard_input.get(): # only press if randKey is enabled
        pyautogui.press(key)

def nudge():
    global running
    if running:
        dx = random.randint(-5,5) # picks random number to nudge mouse random pixels in x direction
        dy = random.randint(-5,5) # now in y direction
        pyautogui.move(dx,dy)
        keyboardPress() # randomly press a key
        window.after(random.randint(5,20)*1000, nudge)

def startFunc():
    global running
    running = True
    status.config(text = "Program initiated.")
    nudge()

def stopFunc():
    global running
    running = False
    status.config(text = "Program paused.")


## create window
window = tk.Tk()
window.geometry("250x250")
window.title("Anti-AFK")
keyboard_input = tk.BooleanVar()

## window widgets
startButton = tk.Button(window, text = "Start", command = startFunc, width = 6, height = 1, font = ("Helvetica", 16, "bold"))
stopButton = tk.Button(window, text = "Stop", command = stopFunc, width = 6, height = 1, font = ("Helvetica", 16, "bold"))
status = tk.Label(window, text = "", font = ("Helvetica", 12, "italic"), width = 16)
keyboardButton = tk.Checkbutton(window, text="Random key toggle", variable=keyboard_input, font=("Helvetica", 12))
label = tk.Label(window, text = "made by louie", font = ("Helvetica", 8, "italic", "bold"))

## formatting
startButton.pack(side = tk.TOP, fill = tk.X, padx = 10, pady = 10)
stopButton.pack(side = tk.TOP, fill = tk.X, padx = 10, pady = 10)
keyboardButton.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
status.pack()
label.pack(side = tk.BOTTOM, padx = 10, pady = 10)


window.mainloop()
