from tkinter import *
from VISUALIZE import Visualise

def max_num(head, sequence):
    for i in sequence:
        if i > head:
            return i


def min_num(head, sequence):
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] < head:
            return sequence[i]


def LOOK(head, sequence):
    Order=[]
    old_head = head
    seek_sequence = []
    seek_operations = 0
    seek_sequence.append(head)
    near_num = max_num(head, sequence)
    for i in range(len(sequence)):
        if near_num > head:
            difference = near_num - head
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = max_num(head, sequence)
        elif near_num < head:
            difference = head - near_num
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = min_num(head, sequence)
            if head == min(sequence):
                break
        if head == max(sequence):
            near_num = min_num(old_head, sequence)
            difference = head - near_num
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = min_num(head, sequence)
    print("Seek Sequence : 	", end=" ")
    for i in seek_sequence:
        Order.append(i)
        if i == min(seek_sequence):
            print(i)
        else:
            print(i, " ==> ", end=" ")
    return [Order, seek_operations]

def fun():
    n = d.get()
    head = int(b.get())
    num2 = c.get()
    n = int(n)
    ready_queue = [int(i) for i in num2.split()]
    ready_queue.sort()
    data = LOOK(head, ready_queue)

    global Order, seek_operations
    Order = data[0]
    seek_operations = data[1]

    print("Total number of seek operations : ", seek_operations)


def fun2():

    Visualise("LOOK", Order, seek_operations)


if __name__ == '__main__':
    root = Tk()
    d = StringVar()
    b = StringVar()
    c = StringVar()
    Label(root, text="n (Enter the no.of disks)").grid(row = 0, column= 0)
    text = Entry(root, textvariable=d, bd= 5).grid(row = 0, column= 1)
    Label(root, text="Enter the initial header position").grid(row= 1, column= 0)
    text1 = Entry(root, textvariable=b, bd= 5).grid(row= 1, column= 1)
    Label(root, text="Enter the disks in ready queue").grid(row= 2, column= 0)
    text2 = Entry(root, textvariable=c, bd = 5).grid(row= 2, column= 1)
    Button(root, text= "submit",bd=4,fg="Orange", command= fun).grid(row= 3, column= 0)
    Button(root, text= "Visualize",bd=4,fg="Orange", command= fun2).grid(row= 3, column= 1)
    Button(root, text="Show Answer",bd= 4,fg="Green", command=root.quit).grid(row=3, column=2)
    root.mainloop()