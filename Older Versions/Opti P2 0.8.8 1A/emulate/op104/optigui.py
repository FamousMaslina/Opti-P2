import tkinter as tk
import pathlib
import os
import sys
import platform
import random
import time
from os import system, name
from time import sleep
import tkinter.filedialog as filedialog
from PIL import Image, ImageDraw
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')








root = tk.Tk()

# Set the window title and size
root.title("Opti P")
root.geometry("640x480")

# Create a canvas to draw the loading screen on
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Draw the loading screen
canvas.create_rectangle(0, 0, 640, 480, fill="light blue")
canvas.create_text(320, 240, text="LoadingGUI", font=("Arial", 24))

# Update the window to show the loading screen
root.update()

# Simulate a long-running task (e.g. loading data from a file)
time.sleep(2)

# Clear the canvas and redraw the main screen
canvas.delete("all")
canvas.create_rectangle(0, 0, 640, 480, fill="white")
canvas.create_text(320, 240, text="Main screen", font=("Arial", 24))
root.destroy()


def exit():
    root.destroy()
    exec(open('opticom.py').read())

def open_drawing_program():
    # Create a new top-level window for the drawing program
    drawing_window = tk.Toplevel(root)
    drawing_window.title("Drawing Program")

    # Create a canvas widget in the window
    canvas = tk.Canvas(drawing_window, width=640, height=480)
    canvas.pack()

    # Create an ImageDraw object to draw on the canvas
    image = Image.new("RGB", (640, 480), "white")
    draw = ImageDraw.Draw(image)

    # Define a function to draw a line on the canvas
    def draw_line(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        draw.line((x1, y1, x2, y2), fill="black", width=3)
        canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

    # Bind the draw_line function to the <B1-


def change_color():
    color = color_picker.get()
    root.configure(bg=color)

def open_color_picker():
    color_picker_window = tk.Toplevel(root)
    color_picker_window.title("Change Color")

    global color_picker
    color_picker = tk.Entry(color_picker_window)
    color_picker.pack()

    change_button = tk.Button(color_picker_window, text="Change", command=change_color)
    change_button.pack()

def calc():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculator")

    # Create the calculator display
    display = tk.Entry(calculator_window)
    display.pack()

    # Create a frame to hold the calculator buttons
    buttons_frame = tk.Frame(calculator_window)
    buttons_frame.pack()

    # Create the buttons
    button_names = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "*", "+", ".", "/", "="
    ]
    buttons = {}
    for button_name in button_names:
        button = tk.Button(buttons_frame, text=button_name)
        button.pack(side=tk.LEFT)
        buttons[button_name] = button

    # Create the logic for the calculator
    def calc(key):
        if key == "=":
            # Compute result
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        elif key == "C":
            display.delete(0, tk.END)
        else:
            # Add key to display
            display.insert(tk.END, key)

    # Assign the calc function to each button
    for key in buttons:
        buttons[key]["command"] = lambda x=key: calc(x)


class Taskbar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(side=tk.BOTTOM, fill=tk.X)

        self.start_button = tk.Menubutton(self, text="Start")
        self.start_menu = tk.Menu(self.start_button, tearoff=0)
        self.start_menu.add_command(label="Color Changer", command=open_color_picker)
        self.start_menu.add_command(label="Calculator", command=calc)
        self.start_menu.add_command(label="Draw", command=open_drawing_program)
        self.start_menu.add_command(label="Return to Command", command=exit)
        self.start_button.pack(side=tk.LEFT)
        self.start_button['menu'] = self.start_menu

        self.system_tray = tk.Frame(self, width=40, height=20)
        self.system_tray.pack(side=tk.RIGHT)
        self.start_button = tk.Menubutton(self, text="Start", bg="#D3D3D3")  # Set the background color to light grey
        self.programs = {}

    def add_program(self, program_name, widget):
        button = tk.Button(self, text=program_name)
        button.pack(side=tk.LEFT)
        self.programs[program_name] = (button, widget)

    def remove_program(self, program_name):
        button, widget = self.programs[program_name]
        button.pack_forget()
        widget.pack_forget()
        del self.programs[program_name]




root = tk.Tk()
root.geometry("640x480")
root.configure(bg="gray")
root.resizable(False, False) 
taskbar = Taskbar(root)
root.mainloop()