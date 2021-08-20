
from tkinter import *
import pandas



def header_of_due_list(xiv):
    # root label
    Label(xiv, text="Products", bg='#17202A', width=30, fg='White',
          font=("times new roman", 20, "bold")).grid(row=1, column=0)
    Label(xiv, text="Sells ৳", bg='#17202A', width=10, fg='White',
          font=("times new roman", 20, "bold")).grid(row=1, column=2)
    Label(xiv, text="Date", bg='#17202A', width=22, fg='white',
          font=("times new roman", 20, "bold")).grid(row=1, column=4)



def d_s(xiv):
    def data():
        data = pandas.read_csv('sell-product.csv')
        l = len(data.Product)
        for i in range(0, l):
            if i%2==0:
                Label(frame, text=data.Product[i], bg='#808B96', width=45, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)

                if data.Sells[i]>=2000:
                    Label(frame, text=data.Sells[i], bg='red', width=25, fg='black',
                          font=("times new roman", 13, "bold")).grid(row=i, column=1)

                else:
                    Label(frame, text=data.Sells[i], bg='#808B96', width=25, fg='black',
                          font=("times new roman", 13, "bold")).grid(row=i, column=1)

                Label(frame, text=data.Date[i], bg='#808B96', width=35, fg='black',
                      font=("times new roman", 12, "bold")).grid(row=i, column=3)
            else:
                Label(frame, text=data.Product[i], bg='#ABB2B9', width=45, fg='black',
                      font=("times new roman", 13, "bold")).grid(row=i, column=0)

                if data.Sells[i]>=2000:
                    Label(frame, text=data.Sells[i], bg='#EC7063', width=25, fg='black',
                          font=("times new roman", 13, "bold")).grid(row=i, column=1)
                else:
                    Label(frame, text=data.Sells[i], bg='#ABB2B9', width=25, fg='black',
                          font=("times new roman", 13, "bold")).grid(row=i, column=1)

                Label(frame, text=data.Date[i], bg='#ABB2B9', width=35, fg='black',
                       font=("times new roman", 12, "bold")).grid(row=i, column=3)

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=980, height=260)

    myframe = Frame(xiv, width=50, height=100, bd=0)
    myframe.place(x=0, y=38)

    canvas = Canvas(myframe)
    frame = Frame(canvas)
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)
    data()


