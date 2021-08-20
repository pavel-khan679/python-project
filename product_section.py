from tkinter import *
import pandas


def header_of_product_list(xiv):
    # root label
    Label(xiv, text="Product", bg='#2E4053', width=14, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=0)
    Label(xiv, text="Price ৳", bg='#2E4053', width=5, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=2)
    Label(xiv, text="Size", bg='#2E4053', width=10, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=3)


def p_d(xiv):
    def data():
        data = pandas.read_csv('Grocery-list.csv')
        l = len(data.Product)
        for i in range(0, l):
            if i%2==0:
                Label(frame, text=data.Product[i], bg='#AEB6BF', width=20, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)
                Label(frame, text=data.Price[i], bg='#AEB6BF', width=14, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=1)
                Label(frame, text=data.Size[i], bg='#AEB6BF', width=10, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=3)
            else:
                Label(frame, text=data.Product[i], bg='#D5DBDB', width=20, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)
                Label(frame, text=data.Price[i], bg='#D5DBDB', width=14, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=1)
                Label(frame, text=data.Size[i], bg='#D5DBDB', width=10, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=3)

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=435, height=421)

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


