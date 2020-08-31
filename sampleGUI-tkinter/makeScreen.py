import tkinter
import os

myWindow = tkinter.Tk()
myWindow.title("Greed Demo")
myWindow.geometry('640x480+80+100')
myWindow['padx'] = 8

label = tkinter.Label(myWindow,text='TkInter Grid Demo')
label.grid(row=0,column=0,columnspan=3)

myWindow.columnconfigure(0, weight=100)
myWindow.columnconfigure(1, weight=1)
myWindow.columnconfigure(2, weight=1000)
myWindow.columnconfigure(3, weight=600)
myWindow.columnconfigure(4, weight=1000)
myWindow.rowconfigure(0, weight=1)
myWindow.rowconfigure(1, weight=10)
myWindow.rowconfigure(2, weight=1)
myWindow.rowconfigure(3, weight=3)
myWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(myWindow)
fileList.grid(row=1, column=0, sticky='nsew',rowspan=2)
fileList.config(border=2, relief="sunken")
for zone in os.listdir('/windows/system32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(myWindow, orient=tkinter.VERTICAL,command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw',rowspan=2)
fileList['yscrollcommand'] = listScroll.set

#frame for the radio buttons
optionFrame= tkinter.LabelFrame(myWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp',value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

#widget to display the result
resultLabel = tkinter.Label(myWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(myWindow)
result.grid(row=2, column=2, sticky='sw')

#Frame for the time spinners
timeFrame = tkinter.LabelFrame(myWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
#time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx']= 36

#frame for date spinners
dateFrame = tkinter.Frame(myWindow)
dateFrame.grid(row=4, column=0, sticky='new')
#date labels
dayLabel = tkinter.Label(dateFrame, text='day')
monthLabel = tkinter.Label(dateFrame, text='month')
yearLabel = tkinter.Label(dateFrame, text='year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to_=31)
monthspin = tkinter.Spinbox(dateFrame, width=5, values=("jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to_=2099)
daySpin.grid(row=1, column=0)
monthspin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

#Buttons
okButton = tkinter.Button(myWindow, text='Ok')
cancle = tkinter.Button(myWindow, text='Cancle', command=myWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancle.grid(row=4, column=4, sticky='w')


myWindow.mainloop()

#print(rbValue.get())
