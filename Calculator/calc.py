import tkinter as tk
import math

def button_click(text):
    if text == "=":
        calculate()
    else:
        current = result_label.get()
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, current + str(text))
    update_button_text()

def calculate():
    expression = result_label.get()
    try:
        result = eval(expression)
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, str(result))
    except:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")
    update_button_text()

def clear():
    result_label.delete(0, tk.END)
    update_button_text()

def calculate_square_root():
    number = float(result_label.get())
    result = math.sqrt(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_exponentiation():
    expression = result_label.get()
    result = eval(expression + "**2")
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_percentage():
    number = float(result_label.get())
    result = number / 100
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_sin():
    angle = float(result_label.get())
    result = math.sin(math.radians(angle))
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_cos():
    angle = float(result_label.get())
    result = math.cos(math.radians(angle))
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_tan():
    angle = float(result_label.get())
    result = math.tan(math.radians(angle))
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_log():
    number = float(result_label.get())
    result = math.log10(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_floor():
    number = float(result_label.get())
    result = math.floor(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_ceil():
    number = float(result_label.get())
    result = math.ceil(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_factorial():
    number = int(result_label.get())
    result = math.factorial(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_absolute():
    number = float(result_label.get())
    result = abs(number)
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(result))
    update_button_text()

def calculate_inverse():
    number = float(result_label.get())
    if number != 0:
        result = 1 / number
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, str(result))
    else:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")
    update_button_text()

def calculate_pi():
    result_label.delete(0, tk.END)
    result_label.insert(tk.END, str(math.pi))
    update_button_text()

def update_button_text():
    buttons = number_buttons + operation_buttons + function_buttons
    for button in buttons:
        button_text = button["text"]
        button.configure(text=button_text, font=button_font)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.config(bg="#36393F")  # Set background color

# Custom font for the buttons and result label
button_font = ("Arial", 14, "bold")
result_font = ("Arial", 24)

# Create a label to display the result
result_label = tk.Entry(window, bg="#36393F", fg="white", font=result_font, justify="right", bd=0)
result_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# Create number buttons
number_buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0), (".", 4, 1)
]

for button_data in number_buttons:
    button_text, row, col = button_data
    button = tk.Button(
        window, text=button_text, command=lambda text=button_text: button_click(text),
        bg="#2C2F33", fg="white", font=button_font, padx=15, pady=10
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Create operation buttons
operation_buttons = [
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
    ("=", 4, 2)
]

for operation_data in operation_buttons:
    operation_text, row, col = operation_data
    button = tk.Button(
        window, text=operation_text, command=lambda text=operation_text: button_click(text),
        bg="#7289DA", fg="white", font=button_font, padx=15, pady=10
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Create function buttons
function_buttons = [
    ("√", 1, 4), ("^2", 2, 4), ("%", 3, 4),
    ("sin", 1, 5), ("cos", 2, 5), ("tan", 3, 5),
    ("log", 4, 4), ("floor", 4, 5),
    ("!", 5, 4), ("|x|", 5, 5),
    ("1/x", 5, 0), ("^", 5, 1),
    ("π", 5, 2)
]

for function_data in function_buttons:
    function_text, row, col = function_data
    button = tk.Button(
        window, text=function_text, command=lambda text=function_text: button_click(text),
        bg="#7289DA", fg="white", font=button_font , padx=15, pady=10
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Create clear button
clear_button = tk.Button(
    window, text="C", command=clear,
    bg="#FF4E4E", fg="white", font=button_font, padx=15, pady=10
)
clear_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

# Create pi button
pi_button = tk.Button(
    window, text="π", command=calculate_pi,
    bg="#2C2F33", fg="white", font=button_font, padx=15, pady=10
)
pi_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

# Configure column and row weights for resizing
for i in range(6):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)

# Start the main event loop
window.mainloop()
