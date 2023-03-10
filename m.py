# import everything from tkinter module
import tkinter as tk
#calucate function to evaluate the provided numbers and returns result of them
def calculate():
    first_number = int(number1_entry.get())
    second_number = int(number2_entry.get())
    operator = int(operator_entry.get())
    # Try and except statement is used for handling the errors like zero division error etc.
    try:

        if operator == 1:
            result = first_number + second_number
            result_label.config(text="result: " + str(result))
        elif operator == 2:
            result = first_number - second_number
            result_label.config(text="result: " + str(result))
        elif operator == 3:
            result = first_number * second_number
            result_label.config(text="result: " + str(result))
        elif operator == 4:
            result = first_number / second_number
            result_label.config(text="result: " + str(result))
        elif operator == 5:
            result = first_number ** second_number
            result_label.config(text="result: " + str(result))
        else:
            result_label.config(text="Invalid Operator")
    except:
        result_label.config(text="Invalid operation")

#  creating the GUI
root = tk.Tk()
#title of GUI
root.title("MY Calc")
#configuring the GUI
root.geometry("300x300")
#creating a label for available operations using widget Label
operator_label = tk.Label(root, text="please select operation-\n\n 1.Addition\n\n 2.Subtraction\n\n 3.Multiplication\n\n 4.Division\n\n 5.power\n")
operator_label.grid(row=0,column=0)
#creating a label for first number using widget Label
number1_label = tk.Label(root, text= "First number:")
number1_label.grid(row=1,column=0)
#first number entry box
number1_entry = tk.Entry(root)
number1_entry.grid(row=1,column=1)
#creating a label for second number using widget Label
number2_label = tk.Label(root, text= "Second number:")
number2_label.grid(row=2,column=0)
#second number entry box
number2_entry = tk.Entry(root)
number2_entry.grid(row=2,column=1)
#creating a label for operation using widget Label
op_label = tk.Label(root, text= "operation:")
op_label.grid(row=3,column=0)
#operation number entry box
operator_entry = tk.Entry(root)
operator_entry.grid(row=3,column=1)
#create a Buttons and place at a particular location inside the root window .
# when user press the button, the command or function affiliated to that button is executed .
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4,column=0)
#creating a label for result using widget Label
result_label = tk.Label(root, text="Result")
result_label.grid(row=5,column=1)
#staring the GUI
root.mainloop()
