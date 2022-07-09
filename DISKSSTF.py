from tkinter import *

def SSTF(head, sequence):
    seek_sequence = []
    seek_operations = 0
    seek_sequence.append(head)
    for i in range(len(sequence)):
        near_num = sequence[
            min(range(len(sequence)), key=lambda i: abs(sequence[i] - head))
        ]
        if head >= near_num:
            difference = head - near_num
            seek_operations += difference
            head = near_num
        if head <= near_num:
            difference = near_num - head
            seek_operations += difference
            head = near_num
        sequence.remove(near_num)
        seek_sequence.append(near_num)
    print("Seek Sequence : 	", end=" ")
    for i in seek_sequence:
        if i == seek_sequence[len(seek_sequence) - 1]:
            print(i)
        else:
            print(i, " ==> ", end=" ")
    return seek_operations

def fun():
    n = d.get()
    head = int(b.get())
    num2 = c.get()
    n = int(n)
    ready_queue = [int(i) for i in num2.split()]
    seek_operations = SSTF(head, ready_queue)

    print("Total number of seek operations : ", seek_operations)


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
    Button(root, text="Show Answer",bd= 4,fg="Green", command=root.quit).grid(row=3, column=1)
    root.mainloop()