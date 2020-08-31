import tkinter


def create_button(text, row, column, height=3, width=7, columnspan=1) :
    return tkinter.Button(myWindow, text=text, height=height, width=width).grid(row=row, column=column, columnspan=columnspan, sticky='w' )

myWindow = tkinter.Tk()
myWindow.title('Calculator challenge')

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

result_text_label = tkinter.StringVar()
tkinter.Label(result_frame, textvariable=result_text_label).grid(row=0, column=0)


create_button('C', 3, 1)
create_button('CE', 3, 2)

create_button('7', 4, 1)
create_button('8', 4, 2)
create_button('9', 4, 3)
create_button('+', 4, 4)

create_button('4', 5, 1)
create_button('5', 5, 2)
create_button('6', 5, 3)
create_button('-', 5, 4)

create_button('1', 6, 1)
create_button('2', 6, 2)
create_button('3', 6, 3)
create_button('*', 6, 4)

create_button('0', 7, 1)
create_button('=', 7, 2, 3, 19, 3)
create_button('/', 7, 4)

myWindow.mainloop()
