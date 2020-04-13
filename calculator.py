from tkinter import *


def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clear_display():
    global operator
    operator = ""
    text_input.set(operator)


def equals():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ""

calculator = Tk()
calculator.title("Calculator")
operator = ""
text_input = StringVar()

textDisplay = Entry(calculator, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                    bg="orange", justify=RIGHT).grid(columnspan=4)

btn7 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", command=lambda:button_click(7), bg="orange").grid(row=1, column=0)
btn8 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:button_click(8), bg="orange").grid(row=1, column=1)
btn9 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:button_click(9), bg="orange").grid(row=1, column=2)
addition = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", command=lambda:button_click('+'), bg="orange").grid(row=1, column=3)
#**************************************************************************************************************************
btn4 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", command=lambda:button_click(4), bg="orange").grid(row=2, column=0)
btn5 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", command=lambda:button_click(5), bg="orange").grid(row=2, column=1)
btn6 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", command=lambda:button_click(6), bg="orange").grid(row=2, column=2)
subtaction = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", command=lambda:button_click('-'), bg="orange").grid(row=2, column=3)
#**************************************************************************************************************************
btn1 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", command=lambda:button_click(1), bg="orange").grid(row=3, column=0)
btn2 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", command=lambda:button_click(2), bg="orange").grid(row=3, column=1)
btn3 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", command=lambda:button_click(3), bg="orange").grid(row=3, column=2)
multiply = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", command=lambda:button_click('*'), bg="orange").grid(row=3, column=3)
#**************************************************************************************************************************
btn0 = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", command=lambda:button_click(0), bg="orange").grid(row=4, column=0)
clear_button = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), command=clear_display, text="C", bg="orange").grid(row=4, column=1)
equals_button = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), command=equals, text="=", bg="orange").grid(row=4, column=2)
divide = Button(calculator, padx=32, pady=32, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", command=lambda:button_click('/'), bg="orange").grid(row=4, column=3)

calculator.mainloop()
