from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from serial import Serial

window = Tk()
window.minsize(900, 500)
window.resizable(False, False)

TextBox = Entry(window, font='Arial 15', width=10)
TextBox.place(relx=0.05, rely=0.12, relwidth=0.4, relheight=0.1)


def SendToPort():
    Data = TextBox.get()
    ser = serial.Serial(port='COM5', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)
    ser.close()
    ser.open()
    ser.write(Data)
    ser.close()

Send = Button(window, font='Arial 15', text='Send', command=SendToPort)
Send.place(relx=0.48, rely=0.12, relwidth=0.2, relheight=0.1)

SerialLabel = Label(window, font='Arial 15', width=10, text='List of Serial Ports')
SerialLabel.place(relx=0.73, rely=0.15, relwidth=0.2, anchor='w')

SerialList = ttk.Combobox(window, font='Arial 15', width=10)
SerialList.place(relx=0.73, rely=0.2, relwidth=0.2, relheight=0.1)

ports = serial.tools.list_ports.comports()
PortList = []
for p in ports:
    PortList.insert(0, p.device)
print(PortList)
num = 0
SerialList['values'] = PortList

ParametersLabel = Label(window, font='Arial 15', width=10, text='Parameters')
ParametersLabel.place(relx=0.73, rely=0.5, relwidth=0.2, anchor='w')

Parameters = Listbox(window, font='Arial 15', width=10)
Parameters.place(relx=0.73, rely=0.55, relwidth=0.2, relheight=0.4)

TerminalLabel = Label(window, font='Arial 15', text='Terminal Window')
TerminalLabel.place(relx=0.05, rely=0.4, relwidth=0.2)

Terminal = Entry(window, font="Arial 15", width=15)
Terminal.place(relx=0.05, rely=0.45, relwidth=0.62, relheight=0.5)


window.mainloop()