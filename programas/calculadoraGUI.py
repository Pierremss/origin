import tkinter as tk # importing the library

window = tk.Tk() #creating th main window
window.title("python calculator :)") #title of window
#window.geometry("400x600")

calculator = "" #this variable will store the operations that user will do in the calculator, it will be a string because we will use the eval() function to calculate the result of the operationd, and the eval() transform the string to math'expression and then calculate the result

def clickButton(value): #this function will be responsible for show the operations at the painel, it will receive the value of the button tha was clicked and add it to the global variable "calculator"
    global calculator
    calculator += str(value)
    textPainel.set(calculator)

def calc(): #this function will be responsible for calculate the result of the operation that user did in calculator, it will use the eval() function to calculate
    global calculator
    try:
        result = str(eval(calculator))
        if calculator == 0:
            calculator = ""
        else:
            calculator = result
        textPainel.set(result)
    except Exception:
        textPainel.set("ERROR")
        calculator = ""

def clean(): #this function will clean the painel and the global variable "calculator"
    global calculator
    calculator = ""
    textPainel.set("Hello!!")
    textPainel.set("")

textPainel = tk.StringVar() #var in real time for the Painel
painel = tk.Entry(window, textvariable=textPainel, font=("Times New Roman", 20), justify="center", state="readonly").grid(row=0, column=0, columnspan=4, sticky="nsew") #creating the Painel

tk.Button(window, text="1", font=("Times New Roman", 20), command=lambda: clickButton(1)).grid(row=1, column=0, sticky="nsew")
tk.Button(window, text="2", font=("Times New Roman", 20), command=lambda: clickButton(2)).grid(row=1, column=1, sticky="nsew")
tk.Button(window, text="3", font=("Times New Roman", 20), command=lambda: clickButton(3)).grid(row=1, column=2, sticky="nsew")
tk.Button(window, text="+", font=("Times New Roman", 20), command=lambda: clickButton("+")).grid(row=1, column=3, sticky="nsew")

tk.Button(window, text="4", font=("Times New Roman", 20), command=lambda: clickButton(4)).grid(row=2, column=0, sticky="nsew")
tk.Button(window, text="5", font=("Times New Roman", 20), command=lambda: clickButton(5)).grid(row=2, column=1, sticky="nsew")
tk.Button(window, text="6", font=("Times New Roman", 20), command=lambda: clickButton(6)).grid(row=2, column=2, sticky="nsew")
tk.Button(window, text="-", font=("Times New Roman", 20), command=lambda: clickButton("-")).grid(row=2, column=3, sticky="nsew")

tk.Button(window, text="7", font=("Times New Roman", 20), command=lambda: clickButton(7)).grid(row=3, column=0, sticky="nsew")
tk.Button(window, text="8", font=("Times New Roman", 20), command=lambda: clickButton(8)).grid(row=3, column=1, sticky="nsew")
tk.Button(window, text="9", font=("Times New Roman", 20), command=lambda: clickButton(9)).grid(row=3, column=2, sticky="nsew")
tk.Button(window, text="x", font=("Times New Roman", 20), command=lambda: clickButton("*")).grid(row=3, column=3, sticky="nsew")

tk.Button(window, text=",", font=("Times New Roman", 20), command=lambda: clickButton(".")).grid(row=4, column=0, sticky="nsew")
tk.Button(window, text="0", font=("Times New Roman", 20), command=lambda: clickButton(0)).grid(row=4, column=1, sticky="nsew")
tk.Button(window, text="C", font=("Times New Roman", 20), command=lambda: clean()).grid(row=4, column=2, sticky="nsew")
tk.Button(window, text="/", font=("Times New Roman", 20), command=lambda: clickButton("/")).grid(row=4, column=3, sticky="nsew")
tk.Button(window, text="=", font=("Times New Roman", 20), command=lambda: calc()).grid(row=5, column=0, columnspan=4, sticky="nsew")

window.mainloop() #this keep the window open until the user close it