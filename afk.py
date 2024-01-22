import tkinter as tk
import random
import time
import pyautogui


# Main program that creates a window, formats widgets, and adds clickable buttons
def main():    
    ## create window and declare some global variables
    global window
    window = tk.Tk()
    window.geometry("250x250")
    window.title("Anti-AFK Tool")
    global keyboard_input
    keyboard_input = tk.BooleanVar()

    ## window widgets
    startButton = tk.Button(window, text = "Start", command = start_func, width = 6, height = 1, font = ("Helvetica", 16, "bold"))
    stopButton = tk.Button(window, text = "Stop", command = stop_func, width = 6, height = 1, font = ("Helvetica", 16, "bold"))
    global status
    status = tk.Label(window, text = "", font = ("Helvetica", 12, "italic"), width = 16)
    keyboardButton = tk.Checkbutton(window, text="Random key toggle", variable=keyboard_input, font=("Helvetica", 12))
    label = tk.Label(window, text = "made by louie", font = ("Helvetica", 8, "italic", "bold"))

    ## formatting
    startButton.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    stopButton.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    keyboardButton.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    status.pack()
    label.pack(side=tk.BOTTOM, padx=10, pady=10)
    
    ## window waits for input
    window.mainloop()


# Function to handle pressing keys
def keyboard_press():
    global keyboard_input
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
    key = random.choice(keys)
    if keyboard_input.get(): # only press if keyboard_input is enabled
        pyautogui.press(key)


# Function to handle mouse movement and calling the keyboard_press function
def nudge():
    global running
    if running:
        dx = random.randint(-5,5) # picks random number to nudge mouse random pixels in x direction
        dy = random.randint(-5,5) # now in y direction
        pyautogui.move(dx,dy)
        keyboard_press() # randomly press a key
        window.after(random.randint(5,20)*1000, nudge)


# Function to start the program and init the nudge function
def start_func():
    global running
    running = True
    status.config(text = "Program initiated.")
    nudge()


# Function that stops the nudge and keyboard_press functions
def stop_func():
    global running
    running = False
    status.config(text = "Program paused.")


# Init program
if __name__ == "__main__":
    main()
