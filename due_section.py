from tkinter import *
import pandas


def header_of_due_list(xiv):
    # root label
    Label(xiv, text="Name", bg='#2E4053', width=21, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=0)
    Label(xiv, text="Due ৳", bg='#2E4053', width=6, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=2)
    Label(xiv, text="Date", bg='#2E4053', width=11, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=4)



def d_s(xiv):
    def data():
        data = pandas.read_csv('product-due-list.csv')
        l = len(data.Name)
        for i in range(0, l):
            if i%2==0:
                Label(frame, text=data.Name[i], bg='#AEB6BF', width=32, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)
                Label(frame, text=data.Due[i], bg='#AEB6BF', width=12, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=1)
                Label(frame, text=data.Date[i], bg='#AEB6BF', width=20, fg='black',
                      font=("times new roman", 12, "bold")).grid(row=i, column=3)
            else:
                Label(frame, text=data.Name[i], bg='#D5DBDB', width=32, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)
                Label(frame, text=data.Due[i], bg='#D5DBDB', width=12, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=1)
                Label(frame, text=data.Date[i], bg='#D5DBDB', width=20, fg='black',
                       font=("times new roman", 12, "bold")).grid(row=i, column=3)

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=589, height=421)

    myframe = Frame(xiv, width=50, height=100, bd=0)
    myframe.place(x=0, y=75)

    canvas = Canvas(myframe)
    frame = Frame(canvas)
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)
    data()


