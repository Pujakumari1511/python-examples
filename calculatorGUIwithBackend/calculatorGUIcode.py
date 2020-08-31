import tkinter

def click_0():
    global input_label
    input_label.set(input_label.get() + "0")


def click_1():
    global input_label
    input_label.set(input_label.get() + "1")


def click_2():
    global input_label
    input_label.set(input_label.get() + "2")


def click_3():
    global input_label
    input_label.set(input_label.get() + "3")

def click_4():
    global input_label
    input_label.set(input_label.get() + "4")


def click_5():
    global input_label
    input_label.set(input_label.get() + "5")


def click_6():
    global input_label
    input_label.set(input_label.get() + "6")


def click_7():
    global input_label
    input_label.set(input_label.get() + "7")


def click_8():
    global input_label
    input_label.set(input_label.get() + "8")


def click_9():
    global input_label
    input_label.set(input_label.get() + "9")


def click_dot():
    global input_label
    input_label.set(input_label.get() + ".")


def click_equalto():
    global input_label
    first_number = ""
    second_number = ""
    operation = None
    result = 0
    for i in input_label.get():
        if i not in ["+", "-", "*", "/"]:
            if operation == None:
                first_number += i
            else:
                second_number += i
        else:
            operation = i


    if operation == '+':
        result = float(first_number) + float(second_number)
    elif operation == '-':
        result = float(first_number) - float(second_number)
    elif operation == 'x':
        result = float(first_number) * float(second_number)
    elif operation == '/':
        try:
            result = float(first_number) / float(second_number)
        except ZeroDivisionError:
            input_label.set("{} can not be divided by zero".format(first_number))
            return
    input_label.set(input_label.get() + "=" + str(result))


def special_charactor(sc):
    global input_label
    if input_label.get() == '' and sc not in ["+", "*", "/"]:
        input_label.set(sc)
    elif input_label.get() not in '/':
        input_label.set(sc)


def click_plus():
    special_charactor("+")


def click_minus():
    special_charactor("-")


def click_multiply():
    special_charactor("*")


def click_divide():
    special_charactor("/")


def click_c():
    global input_label
    input = input_label.get()
    input_label.set(input[: -1])


def click_ce():
    global input_label
    input_label.set("")


def create_button(text, row, column, command) :
    return tkinter.Button(myWindow, text=text, height=3, width=7, command=command).grid(row=row, column=column, columnspan=1, sticky='w' )

myWindow = tkinter.Tk()
myWindow.title('Calculator')

myWindow.geometry('600x450')

myWindow.columnconfigure(0, weight=1)
myWindow.columnconfigure(1, weight=1)
myWindow.columnconfigure(2, weight=1)
myWindow.columnconfigure(3, weight=1)
myWindow.columnconfigure(4, weight=1)
myWindow.columnconfigure(5, weight=10)
myWindow.rowconfigure(0, weight=1)
myWindow.rowconfigure(1, weight=1)
myWindow.rowconfigure(2, weight=1)
myWindow.rowconfigure(3, weight=1)
myWindow.rowconfigure(4, weight=1)
myWindow.rowconfigure(5, weight=1)
myWindow.rowconfigure(6, weight=1)
myWindow.rowconfigure(7, weight=1)


empty_space = tkinter.Frame(myWindow)
empty_space.grid(column=0, row=0, sticky='ns')

label = tkinter.Label(myWindow,text='Calculator')
label.grid(row=0, column=0, columnspan=5)

result_frame = tkinter.Frame(myWindow, relief='sunken', borderwidth=1, background='white')
result_frame.grid(row=1, column=1, sticky='nsew', columnspan=4, rowspan=2)


input_label = tkinter.StringVar()
tkinter.Label(result_frame, textvariable=input_label).grid(row=0, column=0)


create_button('C', 3, 1, click_c)
create_button('CE', 3, 2, click_ce)

create_button('7', 4, 1, click_7)
create_button('8', 4, 2, click_8)
create_button('9', 4, 3, click_9)
create_button('+', 4, 4, click_plus)

create_button('4', 5, 1, click_4)
create_button('5', 5, 2, click_5)
create_button('6', 5, 3, click_6)
create_button('-', 5, 4, click_minus)

create_button('1', 6, 1, click_1)
create_button('2', 6, 2, click_2)
create_button('3', 6, 3, click_3)
create_button('x', 6, 4, click_multiply)

create_button('0', 7, 1, click_0)
create_button('.', 7, 2, click_dot)
create_button('=', 7, 3, click_equalto)
create_button('/', 7, 4, click_divide)


myWindow.mainloop()