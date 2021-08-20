import csv
import time
from tkinter import *

import pandas as pd
import pygame
from PIL import Image, ImageTk

import due_section
# import statistic
# import login
import product_section
import sell_details

pygame.mixer.init()
def play_done():
    pygame.mixer.music.load("done_tone.mp3")
    pygame.mixer.music.play(loops=0)
def play_error():
    pygame.mixer.music.load("error_tone.mp3")
    pygame.mixer.music.play(loops=0)
def play_add():
    pygame.mixer.music.load("add_tone.mp3")
    pygame.mixer.music.play(loops=0)
def play_delete():
    pygame.mixer.music.load("delete_tone.mp3")
    pygame.mixer.music.play(loops=0)


def raise_frame(frame):
    frame.tkraise()


def main_frame():
    window = Tk()
    window.geometry("1100x700+220+20")
    window.resizable(False, False)
    window.title("মুদি দোকান")
    text = "Dashboard"

    # desiginign main frame
    main_frame = Frame(window, bg='#85929E')
    main_frame.place(x=0, y=0, width=1100, height=700)




    #design of login frame


    login_frame = Frame(window, bg='#212F3C')
    login_frame.place(x=0, y=0, width=1100, height=700)

    def log_f(xiv):

        log_label = Label(xiv, text="Username", bg='#212F3C', width=30, fg='yellow',
                          font=("times new roman", 15, "bold"))
        log_label.place(x=700, y=450, height=30, width=200)

        log_label2 = Label(xiv, bg='white')
        log_label2.place(x=757, y=516, height=1, width=200)

        name_entry = Entry(xiv, relief=SOLID, bd=0, fg='white', bg='#212F3C', font=("times new roman", 15, "bold"))
        name_entry.place(x=757, y=485, width=300, height=30)

        pass_label = Label(xiv, text="Password", bg='#212F3C', width=30, fg='yellow',
                           font=("times new roman", 15, "bold"))
        pass_label.place(x=700, y=520, height=30, width=200)

        log_label3 = Label(xiv, bg='white')
        log_label3.place(x=757, y=586, height=1, width=200)

        pass_entry = Entry(xiv, relief=SOLID, bd=0, bg='#212F3C', fg='white', font=("times new roman", 15, "bold"))
        pass_entry.place(x=757, y=555, width=300, height=30)



        d1_frame = Frame(xiv, bg='#6600CC')
        d1_frame.place(x=10, y=-1, width=265, height=400)



        d2_frame = Frame(xiv, bg='#CC0099')
        d2_frame.place(x=285, y=0, width=265, height=300)


        d3_frame = Frame(xiv, bg='#FF6600')
        d3_frame.place(x=560, y=0, width=265, height=200)

        d3_frame = Frame(xiv, bg='#CCFF00')
        d3_frame.place(x=835, y=0, width=255, height=100)




        def checker():
            n=name_entry.get()
            p=pass_entry.get()
            if n=="user" and p=="user":
                play_done()
                raise_frame(main_frame)
            else:
                play_error()
                log_label = Label(xiv,
                                  text="আপনার ইউজারনেম অথবা পাসওয়ার্ড ভুল !\nআপাতত ডেভলপারের সাথে যোগাযোগ করুন\nকারণ,রিসেট করার জন্যে সফটয়া্রের ভেতরে\n    আর কোন অপশন নেই!",
                                  bg='#212F3C', width=30, fg='yellow',
                                  font=("times new roman", 20, "bold"))
                log_label.place(x=50, y=400, height=250, width=600)





        login_button = Button(login_frame, text='    Login    ', relief=SOLID, font=("times new roman", 15, "bold"),
                              bd=0,
                              bg='green', fg='white', command=lambda: [checker()])
        login_button.place(x=757, y=620, width=200, height=30)


    log_f(login_frame)










    title = Label(main_frame, text=text, bg='#1B2631', fg='white', font=("times new roman", 38, "bold"), width=1100,
                  height=1)
    title.pack(side=TOP)

    window.configure(bg='lavender')

    # design frame1
    design_frame1 = Frame(main_frame, bg='#283747')
    design_frame1.place(x=0, y=64, width=1100, height=300)

    # Bill list frame
    product_frame = Frame(main_frame, relief=RIDGE, bg="white")
    product_frame.place(x=10, y=90, width=457, height=500)

    # due list frame
    due_frame = Frame(main_frame, relief=RIDGE, bg="white")
    due_frame.place(x=480, y=90, width=610, height=500)

    # product title
    P_title = Label(product_frame, text="Product Details", bg='#17202A', width=30, fg='white',
                    font=("times new roman", 20, "bold"))
    P_title.grid(row=0, columnspan=55, pady=0)

    # due title
    D_title = Label(due_frame, text="Due Details", bg='#17202A', width=39, fg='white',
                    font=("times new roman", 20, "bold"))
    D_title.grid(row=0, columnspan=55, pady=0)

    # list of product in product frame
    def p_refresh():
        product_section.header_of_product_list(product_frame)
        product_section.p_d(product_frame)
    p_refresh()

    # list of due in due frame
    def d_refresh():
        due_section.header_of_due_list(due_frame)
        due_section.d_s(due_frame)
    d_refresh()


    #design of statistic frame
    # def stat_frame():
    #     stat_frame = Frame(window, bg='red')
    #     stat_frame.place(x=0, y=0, width=1100, height=700)

    #     statistic.stat(stat_frame)



    #     back = Button(window, text='    Back    ', relief=SOLID, font=("times new roman", 15, "bold"), bd=0,
    #                   bg='#5D6D7E', fg='black', command=after_pressing_browse_more)
    #     back.place(x=0, y=665)

    #     back_main = Button(window, text='    Back to main menu    ', relief=SOLID, font=("times new roman", 15, "bold"),
    #                        bd=0,
    #                        bg='#5D6D7E', fg='black', command=lambda: raise_frame(main_frame))
    #     back_main.place(x=900, y=665)




    # after explore option
    def after_pressing_browse_more():
        def SAD():
            search_add_frame=Frame(window,bg='#212F3D')
            search_add_frame.place(x=0, y=0, width=1100, height=700)




            #function of full search
            def main_design(xiv):
                # product section
                title1 = Label(xiv, text="Product Section", bg='#212F3D', fg='white',
                               font=("times new roman", 38, "bold"), width=1100, height=1)
                title1.pack(side=TOP)

                title2 = Label(xiv, text="Due section", bg='#212F3D', fg='white', font=("times new roman", 38, "bold"),
                               width=1100, height=1)
                title2.place(x=0, y=330, height=70, width=1100)

                p_entry1 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                p_entry1.place(x=50, y=80, width=700, height=30)

                def search_work():
                    df = pd.read_csv("Grocery-list.csv")
                    value = p_entry1.get()
                    l=len(df.Product)
                    flag=0
                    for i in range(l):
                        if value==df.Product[i]:
                            name=value
                            price=df.Price[i]
                            size=df.Size[i]
                            flag =1

                    if flag==1:
                        play_add()
                        lst = [name, '----------', price, "taka", '------------------------', size]
                        p_answer.delete(1.0, END)
                        p_answer.insert(INSERT,lst)

                    else:
                        play_add()
                        p_answer.delete(1.0, END)
                        p_answer.insert(INSERT,"ধুর, এমন কোন নাম ই নাই")




                search_button = Button(xiv, text='Search',command=search_work, relief=SOLID, font=("times new roman", 13, "bold"), bd=0,
                                       bg='white', fg='black')
                search_button.place(x=760, y=81, width=90)


                p_answer = Text(xiv, wrap=WORD, font=("times new roman", 20, "bold"))
                p_answer.place(x=50, y=120, height=100, width=800)



                p_entry2 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                p_entry2.place(x=50, y=250, width=380, height=38)

                p_entry3 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                p_entry3.place(x=440, y=250, width=150, height=38)

                p_entry4 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                p_entry4.place(x=600, y=250, width=150, height=38)

                # work for product section

                def add_product():
                    value1 = p_entry2.get()
                    value2 = p_entry3.get()
                    value3 = p_entry4.get()



                    if value2.isdigit():
                        play_add()
                        with open("Grocery-list.csv", "a") as csvfile:
                            fildnames = ["Product", "Price", "Size"]
                            writer = csv.DictWriter(csvfile, fieldnames=fildnames)
                            writer.writerow({"Product": value1, "Price": value2, "Size": value3})



                add_button = Button(xiv, text='Add', command=lambda: [add_product(),SAD(),p_refresh()], relief=SOLID,
                                    font=("times new roman", 13, "bold"), bd=0,
                                    bg='white', fg='black')
                add_button.place(x=760, y=250, width=90, height=38)


                def for_delete_product():
                    name = p_entry1.get()
                    lines = list()

                    with open('Grocery-list.csv', 'r') as readFile:
                        reader = csv.reader(readFile)
                        for row in reader:
                            lines.append(row)
                            for field in row:
                                if field == name:
                                    lines.remove(row)
                                    play_delete()

                    with open('Grocery-list.csv', 'w') as writeFile:
                        writer = csv.writer(writeFile)
                        writer.writerows(lines)




                dlt_button = Button(xiv, text='Delete',command=lambda :[for_delete_product(),p_refresh(),SAD()],relief=SOLID, font=("times new roman", 13, "bold"), bd=0,
                                    bg='#E74C3C', fg='black')
                dlt_button.place(x=880, y=120, width=180, height=100)






                # due section         #########################
                d_entry1 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                d_entry1.place(x=50, y=80 + 340, width=700, height=30)

                #due list search
                def search_work2():
                    df = pd.read_csv("product-due-list.csv")
                    value = d_entry1.get()
                    l=len(df.Name)
                    flag=0
                    price=0
                    for i in range(l):
                        if value==df.Name[i]:
                            name=value
                            price+=df.Due[i]
                            size=df.Date[i]
                            flag =1

                    if flag==1:
                        play_add()
                        lst = [name, '----------', price, "taka", '------------------------', size]
                        d_answer.delete(1.0, END)
                        d_answer.insert(INSERT,lst)
                        if price>1000:
                            d_answer.insert(INSERT,"    এই বাটপার এর কাছে ১০০০ টাকার বেশি পাওন যায় !")

                    else:
                        play_add()
                        d_answer.delete(1.0, END)
                        d_answer.insert(INSERT,"ধুর, এমন কোন নাম ই নাই")



                search_button = Button(xiv, text='Search',command=search_work2, relief=SOLID, font=("times new roman", 13, "bold"), bd=0,
                                       bg='white',
                                       fg='black')
                search_button.place(x=760, y=81 + 340, width=90)

                d_answer = Text(xiv, wrap=WORD, font=("times new roman", 20, "bold"))
                d_answer.place(x=50, y=120 + 340, height=100, width=800)




                def for_delete_product2():
                    name = d_entry1.get()
                    lines = list()

                    with open('product-due-list.csv', 'r') as readFile:
                        reader = csv.reader(readFile)
                        for row in reader:
                            lines.append(row)
                            for field in row:
                                if field == name:
                                    lines.remove(row)
                                    play_delete()

                    with open('product-due-list.csv', 'w') as writeFile:
                        writer = csv.writer(writeFile)
                        writer.writerows(lines)



                dlt_button = Button(xiv, text='এই\nব্যাক্তির\nটাকা\nশোধ',command=lambda :[for_delete_product2(),d_refresh(),SAD()], relief=SOLID, font=("times new roman", 13, "bold"), bd=0,
                                    bg='#E74C3C',
                                    fg='black')
                dlt_button.place(x=880, y=120 + 340, width=180, height=100)

                d_entry2 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                d_entry2.place(x=50, y=250 + 340, width=380, height=38)

                d_entry3 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                d_entry3.place(x=440, y=250 + 340, width=150, height=38)

                d_entry4 = Entry(xiv, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
                d_entry4.place(x=600, y=250 + 340, width=150, height=38)


                #due list add customer
                def add_product2():
                    value1 = d_entry2.get()
                    value2 = d_entry3.get()
                    value3 = d_entry4.get()



                    if value2.isdigit():
                        play_add()
                        with open("product-due-list.csv", "a") as csvfile:
                            fildnames = ["Name", "Due", "Date"]
                            writer = csv.DictWriter(csvfile, fieldnames=fildnames)
                            writer.writerow({"Name": value1, "Due": value2, "Date": value3})



                add_button = Button(xiv, text='Add',command=lambda :[add_product2(),d_refresh(),SAD()], relief=SOLID, font=("times new roman", 13, "bold"), bd=0,
                                    bg='white', fg='black')
                add_button.place(x=760, y=250 + 340, width=90, height=38)










            #design frame calling
            main_design(search_add_frame)

            back = Button(search_add_frame, text='    Back    ', relief=SOLID, font=("times new roman", 15, "bold"), bd=0,
                          bg='#808B96', fg='black', command=after_pressing_browse_more)
            back.place(x=0, y=665)

            back_main = Button(search_add_frame, text='    Back to main menu    ', relief=SOLID,
                               font=("times new roman", 15, "bold"), bd=0,
                               bg='#808B96', fg='black', command=lambda: raise_frame(main_frame))
            back_main.place(x=900, y=665)



        def sell():

            def total_sell():
                data = pd.read_csv('sell-product.csv')
                l = len(data.Sells)
                sum = 0
                for i in range(l):
                    sum += data.Sells[i]
                return sum


            sell_frame=Frame(window,bg='#273746')
            sell_frame.place(x=0,y=0,width=1100,height=700)

            title = Label(sell_frame, text='Sell Hisrory', bg='#17202A', fg='white', font=("times new roman", 38, "bold"),width=1100,height=1)
            title.pack(side=TOP)

            #inside sell frame
            design_frame_s=Frame(sell_frame,bg="gray")
            design_frame_s.place(x=50,y=150,width=1000,height=300)

            #sell details from another class
            sell_details.header_of_due_list(design_frame_s)
            sell_details.d_s(design_frame_s)

            #entry box
            entry1 = Entry(sell_frame,relief=SOLID,bd=0,bg='white',font=("times new roman",15, "bold"))
            entry1.place(x=50, y=480, width=400, height=30)

            entry1_label=Label(sell_frame,text="Product Name",relief=SOLID,bd=0,bg='#273746',font=("times new roman",15, "bold"),fg="white")
            entry1_label.place(x=50,y=455,width=400,height=20)

            entry2 = Entry(sell_frame, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
            entry2.place(x=455, y=480, width=200, height=30)

            entry2_label = Label(sell_frame, text="Taka", relief=SOLID, bd=0, bg='#273746',
                                 font=("times new roman", 15, "bold"), fg="white")
            entry2_label.place(x=350, y=455, width=400, height=20)

            entry3 = Entry(sell_frame, relief=SOLID, bd=0, bg='white', font=("times new roman", 15, "bold"))
            entry3.place(x=660, y=480, width=300, height=30)

            entry3_label = Label(sell_frame, text="Date", relief=SOLID, bd=0, bg='#273746',
                                 font=("times new roman", 15, "bold"), fg="white")
            entry3_label.place(x=640, y=455, width=400, height=20)


            def showing_total():
                x=total_sell()
                text= 'Total',x
                total_label = Label(sell_frame, text=text, relief=SOLID, bd=0, bg='#273746',
                                     font=("times new roman", 18, "bold"), fg="yellow")
                total_label.place(x=480, y=550, width=200, height=20)

            showing_total()


            errase_all_button= Button(sell_frame,bg='red',text='Delete All Data',fg='white',bd=0,font=("italic",15,"bold"))
            errase_all_button.place(x=480, y=600, width=200, height=60)
            def ad():
                value1= entry1.get()
                value2=entry2.get()
                value3=entry3.get()

                if value2.isdigit():
                    play_add()
                    with open("sell-product.csv", "a") as csvfile:
                        fildnames = ["Product", "Sells", "Date"]
                        writer = csv.DictWriter(csvfile, fieldnames=fildnames)
                        writer.writerow({"Product": value1, "Sells": value2, "Date": value3})




            add_button = Button(sell_frame,command=lambda:[ad(),sell()], bg='black', text='Add', fg='white', bd=0, font=("italic", 15, "bold"))
            add_button.place(x=965, y=479, width=88, height=32)





            back = Button(window, text='    Back    ', relief=SOLID, font=("times new roman",15, "bold"), bd=0,
                                 bg='#808B96', fg='black', command=after_pressing_browse_more)
            back.place(x=0, y=665)

            back_main = Button(window, text='    Back to main menu    ', relief=SOLID, font=("times new roman", 15, "bold"), bd=0,
                          bg='#808B96', fg='black',command=lambda:raise_frame(main_frame))
            back_main.place(x=900, y=665)



        pic = Image.open('blur_back.png')

        canvas = Canvas(window,width=1104, height=400, bg='blue')
        canvas.place(x=-3, y=-3)

        canvas.image = ImageTk.PhotoImage(pic)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

        # browse frame design
        # browse_frame = Frame(window, bg='#273746')
        # browse_frame.place(x=0, y=300, width=1100, height=400)

        browse_frame = Frame(window, bg='#212F3D')
        browse_frame.place(x=0, y=400, width=1100, height=400)

        browse_frame = Frame(window, bg='#1C2833')
        browse_frame.place(x=0, y=500, width=1100, height=400)

        browse_frame = Frame(window, bg='#17202A')
        browse_frame.place(x=0, y=600, width=1100, height=400)

        #new browsing button
        sell_button= Button(window, text='Total sells',relief=SOLID,activebackground="#273746",font=("times new roman", 25, "italic bold"),bd=0,bg='#273746',fg='white', command=sell)
        sell_button.place(x=0, y=400)

        search_button = Button(window, text='Search / Add / Delete', relief=SOLID,bd=0,bg='#1C2833',fg='white', font=("times new roman", 25, "italic bold"),
                             command=SAD,activebackground="#1C2833")
        search_button.place(x=0, y=500)

        # stat_button = Button(window, text='Statistics', relief=SOLID,bd=0,bg='#212F3D',fg='white', font=("times new roman", 25, "italic bold"),
        #                        command=stat_frame,activebackground="#212F3D")
        # stat_button.place(x=0, y=400)


        #back button
        more_button = Button(window, text='Back to Dashboard', relief=SOLID,bg='#17202A',fg='white', font=("times new roman", 25, "italic bold"), bd=0,
                             command=lambda: raise_frame(main_frame),activebackground="#17202A")
        more_button.place(x=0, y=600)



    # explore button
    b = Button(main_frame, text="Browse More", bg="black", relief=SOLID, fg='white', bd=0,
               font=("times new roman", 25, "bold"), command=after_pressing_browse_more)
    #b.grid(row=55, column=2, sticky=W)
    b.place(x=0, y=650,height=50,width=1100)

    raise_frame(login_frame)

    window.mainloop()


main_frame()  # running main frame


