from tkinter import *
from subprocess import *

def func():
    proc = Popen("DISKFCFS.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func1():
    proc = Popen("DISKSSTF.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func2():
    proc = Popen("DISKLOOK.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func3():
    proc = Popen("DISKSCAN.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)


if __name__ == '__main__':
    Master = Tk()
    label1 = Label(Master, text="HELLO!  Welcome to Disk Scheduling Calculator")
    label1.pack()
    frame = Frame(Master)
    frame.pack()

    Button(frame, text="FCFS",bd= 4,padx=20,activeforeground="blue", command=func).grid(row=0, column=0, padx= 20, pady=8)
    Button(frame, text="SSTF",bd= 4,padx=20,activeforeground="blue",command= func1).grid(row=0, column= 1, padx = 20, pady=8)
    Button(frame, text="LOOK",bd= 4,padx=20,activeforeground="blue", command=func2).grid(row=0, column=2, padx=20, pady=8)
    Button(frame, text="SCAN",bd= 4,padx=20,activeforeground="blue", command=func3).grid(row=0, column=3, padx=20, pady=8)

    output = Text(Master, width=100, height=20)
    output.pack()
    Master.mainloop()