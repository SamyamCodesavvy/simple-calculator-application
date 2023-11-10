# Importing necessary libraries
from tkinter import *
# Defining font and color variables
fontname1 = "Courier"
fontname2 = "Arial"
bg_color1 = "#c1c7c9"
bg_color2 = "#a62c2b"
bg_color3 = "#000000"
bg_color4 = "#ffffff"
bg_color5 = "#6495ed"
# Function to clear the display when CLEAR ALL button is clicked
def clear_all():
    display.delete(0, END)
# Function to undo the last character when UNDO button is clicked
def on_undo():
    expression = display.get()
    if len(expression):
        new_expression = expression[:-1]
        clear_all()
        display.insert(0, new_expression)
    else:
        clear_all()
        display.insert(0, "Nothing to undo")
# Function to handle button clicks except for buttons CLEAR ALL and UNDO
def on_click(each_button):
    new = str(display.get())
    display.delete(0, END)
    display.insert(0, new+each_button)
# Function to evaluate the expression
def calc_evaluate():
    try:
        expression = display.get()
        # Replace "÷" with "/", "×" with "*", and "–" with "-" to match Python's syntax
        expression = expression.replace("÷", "/").replace("×", "*").replace("–", "-")
        value = eval(expression)
        display.delete(0, END)
        display.insert(0, str(value))
    except ZeroDivisionError:
        display.delete(0, END)
        display.insert(0, "Divide By Zero!")
    except SyntaxError:
        display.delete(0, END)
        display.insert(0, 'Invalid Syntax')
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error Occurred")
# Creating the main application window
root = Tk()
root.resizable(False, False)
root.iconbitmap("calculator_icon.ico")
root.title("Simple Calculator App")
root.config(bg="#373d3f", padx=10, pady=10)
# Creating the entry widget for calculator
display = Entry(root,font=(fontname1, 20, "bold", "italic"), justify=RIGHT, width=18, borderwidth=10, background=bg_color3, highlightbackground=bg_color4, highlightcolor=bg_color4, highlightthickness=2, insertbackground=bg_color4, foreground=bg_color4)
display.grid(row=0, column=0, columnspan=4, pady=10)
# Giving keyboard focus i.e. start typing text into it without clicking on it with the mouse
display.focus_set()
# Defining list of buttons available in the calculator and configurations
button_list = ["C l e a r   A l l", "U n d o", "7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "+", "0", ".", "=", "–"]
# Creating buttons by looping through the list
for each_button in button_list:
    if each_button == "C l e a r   A l l":
        Button(root, text=each_button, width=11, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color2, foreground=bg_color4, activebackground=bg_color1, command=clear_all).grid(row=5, column=0, columnspan=2, ipadx=1, ipady=5, pady=20, padx=12)
    elif each_button == "U n d o":
        Button(root, text=each_button, width=11, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color5, foreground=bg_color4, activebackground=bg_color1, command=lambda button=each_button: on_undo()).grid(row=5, column=2, columnspan=2, ipadx=1, ipady=5, pady=20, padx=12)
    elif each_button == "7":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=6, column=0)
    elif each_button == "8":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=6, column=1)
    elif each_button == "9":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=6, column=2)
    elif each_button == "÷":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=6, column=3)
    elif each_button == "4":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=7, column=0, pady=23)
    elif each_button == "5":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=7, column=1, pady=23)
    elif each_button == "6":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=7, column=2, pady=23)
    elif each_button == "×":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=7, column=3, pady=23)
    elif each_button == "1":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=8, column=0, pady=2)
    elif each_button == "2":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=8, column=1, pady=2)
    elif each_button == "3":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=8, column=2, pady=2)
    elif each_button == "+":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=8, column=3, pady=2)
    elif each_button == "0":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=9, column=0, pady=23)
    elif each_button == ".":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=9, column=1, pady=23)
    elif each_button == "=":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=calc_evaluate).grid(row=9, column=2, pady=23)
    elif each_button == "–":
        Button(root, text=each_button, width=4, font=(fontname2, 15, "bold"), borderwidth=3, bg=bg_color3, foreground=bg_color4, command=lambda button=each_button: on_click(button)).grid(row=9, column=3, pady=10)
# Setting the window position on screen and starting the main event loop
root.geometry("+420+80")
root.mainloop()