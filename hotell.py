from tkinter import *
from tkinter import font
import tkinter.messagebox as msgbox
class Rooms:
    def __init__(self, number, name):
        self.number = number
        self.name = name
"""
Lists of all rooms 
and a main list containing all other lists 
"""
list_1room = [Rooms("1.1", "Available"), Rooms("1.2", "Available"), Rooms("1.3", "Available"), Rooms("1.4", "Available"), Rooms("1.5", "Available")]
list_2room = [Rooms("2.1", "Available"), Rooms("2.2", "Available"), Rooms("2.3", "Available"), Rooms("2.4", "Available"), Rooms("2.5", "Available")]
list_3room = [Rooms("3.1", "Available"), Rooms("3.2", "Available"), Rooms("3.3", "Available"), Rooms("3.4", "Available"), Rooms("3.5", "Available")]
list_4room = [Rooms("4.1", "Available"), Rooms("4.2", "Available"), Rooms("4.3", "Available"), Rooms("4.4", "Available"), Rooms("4.5", "Available")]
all_rooms = [list_1room, list_2room, list_3room, list_4room]

def addToProgram():
    t = open("test.txt", "r")
    num_1 = 0
    num_2 = 0
    num_3 = 0
    num_4 = 0
    for x in t.readlines():
        
        if x[0] == "1":
            writeIThink(x, list_1room, num_1)
            num_1 = num_1 + 1
        
        if x[0] == "2":
            writeIThink(x, list_2room, num_2)
            num_2 = num_2 + 1

        if x[0] == "3":
            writeIThink(x, list_3room, num_3)
            num_3 = num_3 + 1

        if x[0] == "4":
            writeIThink(x, list_4room, num_4)
            num_4 = num_4 + 1
    t.close()

def writeIThink(i, sel_list, u):
    x = i
    y = u
    e = len(x)
    m = x[:3]
    sel_list[y].number = m
    r = x[4:e-1]
    sel_list[y].name = r

class Main:
    def __init__(self, root):
        root.wm_title("HOTELLET")
        root.minsize(750, 500)
        root.maxsize(750, 750)
        root.pic = PhotoImage(file = "sunhotel.png")
        bg_label = Label(root, image=root.pic)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        addToProgram()

        def roomInput(v):
            for x in range(0, 4): #Runs through the available rooms of the kind and if it detects an available it changes then breaks the for loop
                if v[x].name == "Available":
                    v[x].name = "Taken(" + "hej" + ")"
                    break
            else:
                print("Alla rum av denna typ är tagna")


        #Incheckning:
        #Personlig information
        def name():
            btnCheckIn.grid_forget()
            btnCheckOut.grid_forget()
            btnShow.grid_forget()
            btnQuit.grid_forget()
            lblChooseRooms.grid_forget()
            lblPersonalInfo.grid(row=2, pady=2)
            entryName.grid(row=3, pady=2, sticky=E, padx=200)
            entryAge.grid(row=4, pady=2, sticky=E, padx=200)
            entryNumber.grid(row=5, pady=2, sticky=E, padx=200)
            btnContinue.grid(row=6, pady=2)
            lblName.grid(row=3, sticky=W, padx=200)
            lblAge.grid(row=4, sticky=W, padx=200)
            lblNumber.grid(row=5, sticky=W, padx=200)

        #Rumval
        def pressbtn():
            lblPersonalInfo.grid_forget()
            entryName.grid_forget()
            entryAge.grid_forget()
            entryNumber.grid_forget()
            lblName.grid_forget()
            lblAge.grid_forget()
            lblNumber.grid_forget()
            btnContinue.grid_forget()
            btnYes.grid_forget()
            btnNo.grid_forget()
            btn1Room.grid(row=3, padx=2.5, pady=2)
            btn2Room.grid(row=4, padx=2.5, pady=2)
            btn3Room.grid(row=5, padx=2.5, pady=2)
            btn4Room.grid(row=6, padx=2.5, pady=2)
            lblChooseRooms.grid(row=2, pady=2)
            lblMoreRooms.grid_forget()
            
            
            


        #Mer rum
        def pressNumRooms(v):
            roomInput(v)
            btn1Room.grid_forget()
            btn2Room.grid_forget()
            btn3Room.grid_forget()
            btn4Room.grid_forget()
            lblMoreRooms.grid(row=2, pady=2)
            btnYes.grid(sticky=W, row=3, padx=200)
            btnNo.grid(sticky=E, row=3, padx=200)
            

            
            

        #Huvudmeny
        def mainmenu():
            lblMoreRooms.grid_forget()
            btnYes.grid_forget()
            btnNo.grid_forget()
            btnContinueCheckout.grid_forget()
            HotelName.grid(row=1, padx=200, pady=2)
            btnCheckIn.grid(row=2, pady=2)
            btnCheckOut.grid(row=3, pady=2)
            btnShow.grid(row=4, pady=2)
            btnQuit.grid(row=5, pady=2)
            lblChooseRoomsCheckout.grid_forget()
            btn1RoomCheckout.grid_forget()
            btn2RoomCheckout.grid_forget()
            btn3RoomCheckout.grid_forget()
            btn4RoomCheckout.grid_forget()
            lblCheckout.grid_forget()
            btnCheckoutAll.grid_forget()
            btnCheckoutOne.grid_forget()
            """
            Method for writing and changing the list of available and 
            taken rooms
            """
            t = open("test.txt", "w")
            t.write("One bed rooms\n")
            for x in list_1room:
                t.write(x.number + " " + x.name + "\n")
            t.write("\nTwo bed rooms\n")
            for x in list_2room:
                t.write(x.number + " " + x.name + "\n")
            t.write("\nThree bed rooms\n")
            for x in list_3room:
                t.write(x.number + " " + x.name + "\n")
            t.write("\nFour bed rooms\n")
            for x in list_4room:
                t.write(x.number + " " + x.name + "\n")
            t.close()

        def nameCheckout():
            btnCheckIn.grid_forget()
            btnCheckOut.grid_forget()
            btnShow.grid_forget()
            btnQuit.grid_forget()
            lblPersonalName.grid(row=2, pady=2)
            entryName.grid(row=3, pady=2, sticky=E, padx=200)
            lblName.grid(row=3, sticky=W, padx=200)
            btnContinueCheckout.grid(row=6, pady=2)

        def CheckOut2():
            lblPersonalName.grid_forget()
            entryName.grid_forget()
            lblName.grid_forget()
            btnContinueCheckout.grid_forget()
            lblCheckout.grid(row=2, pady=2)
            btnCheckoutAll.grid(sticky=W, row=3, padx=200)
            btnCheckoutOne.grid(sticky=E, row=3, padx=200)

        def CheckOut3():
            lblCheckout.grid_forget()
            btnCheckoutAll.grid_forget()
            btnCheckoutOne.grid_forget()
            lblChooseRoomsCheckout.grid(row=2, pady=2)
            btn1RoomCheckout.grid(row=3, padx=2.5, pady=2)
            btn2RoomCheckout.grid(row=4, padx=2.5, pady=2)
            btn3RoomCheckout.grid(row=5, padx=2.5, pady=2)
            btn4RoomCheckout.grid(row=6, padx=2.5, pady=2)
                    

        #Personlig info
        lblPersonalInfo = Label(root, text="Skriv in information", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        entryName = Entry(root, width=32, font="sans-serif 10 bold", bg="lightblue")
        entryAge = Entry(root, width=32, font="sans-serif 10 bold", bg="lightblue")
        entryNumber = Entry(root, width=32, font="sans-serif 10 bold", bg="lightblue")
        lblName = Label(root, text="Namn: ", height=1, width=10, bg="lightblue")
        lblAge = Label(root, text="Ålder: ", height=1, width=10, bg="lightblue")
        lblNumber = Label(root, text="Nummer: ", height=1, width=10, bg="lightblue")
        btnContinue = Button(root, width=40, height=5, font="sans-serif 10 bold", bg="lightblue", text="Fortsätt", command=pressbtn)
        
        #Rumval
        lblChooseRooms = Label(root, text="Välj typ av rum", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        btn1Room = Button(root, text="1 Person", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=pressNumRooms(list_1room))
        btn2Room = Button(root, text="2 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=pressNumRooms(list_2room))
        btn3Room = Button(root, text="3 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=pressNumRooms(list_3room))
        btn4Room = Button(root, text="4 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=pressNumRooms(list_4room))
        
        
        #Mer rum
        lblMoreRooms = Label(root, text="Vill du boka ett till rum?", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        btnYes = Button(width=20, height=5, text="Ja", bg="lightblue", font="sans-serif 10 bold", command=pressbtn)
        btnNo = Button(width=20, height=5, text="Nej", bg="lightblue", font="sans-serif 10 bold", command=mainmenu)

        #Utcheckning
        lblPersonalName = Label(root, text="Skriv in ditt namn", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        btnContinueCheckout = Button(root, width=40, height=5, font="sans-serif 10 bold", bg="lightblue", text="Fortsätt", command=CheckOut2)
        lblCheckout = Label(root, text="alla eller ett", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        btnCheckoutAll = Button(width=20, height=5, text="Alla", bg="lightblue", font="sans-serif 10 bold", command=mainmenu)
        btnCheckoutOne = Button(width=20, height=5, text="Ett", bg="lightblue", font="sans-serif 10 bold", command=CheckOut3)
        lblChooseRoomsCheckout = Label(root, text="Välj typ av rum", width=40, height=5, font="sans-serif 10 bold", bg="lightblue")
        btn1RoomCheckout = Button(root, text="1 Person", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=mainmenu)
        btn2RoomCheckout = Button(root, text="2 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=mainmenu)
        btn3RoomCheckout = Button(root, text="3 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=mainmenu)
        btn4RoomCheckout = Button(root, text="4 Personer", width=40, height=2, font="sans-serif 10 bold", bg="lightblue", command=mainmenu)


        #Huvudmeny
        HotelName = Label(text="Hotellet", height=5, width=20, font="times 20 italic bold underline", bg="lightblue")
        HotelName.grid(row=1, padx=200, pady=2)
        
        btnCheckIn = Button(text="INCHECKNING", width=40, height=5, bg="lightblue", font="sans-serif 10 bold", command=name)
        btnCheckIn.grid(row=2, pady=2)

        btnCheckOut = Button(text="UTCHECKNING", width=40, height=5, bg="lightblue", font="sans-serif 10 bold", command=nameCheckout)
        btnCheckOut.grid(row=3, pady=2)
        
        btnShow = Button(text="VISA BOENDE", width=40, height=5, bg="lightblue", font="sans-serif 10 bold")
        btnShow.grid(row=4, pady=2)

        btnQuit = Button(text="AVSLUTA", width=40, height=5, bg="red", font="sans-serif 10 bold", command=root.destroy)
        btnQuit.grid(row=5, pady=2)


        
        #1. Vad heter du?
        #2. Avboka alla rum eller ett rum.
        #3. Avbokar alla rum eller välj vilket slags rum.

        
"""
class Room():
    def __init__(self, size):
        self.size = size

class User():
    def __init__(self, firstName, lastName, phoneNumber, age):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.age = age

Rooms1 = []
Rooms2 = []
Rooms3 = []
Rooms4 = []

while True:
    print("Skriv hur många besökare som checkar in.")
    antPers = input(": ")
    if antPers == "1":
        pass
    elif antPers == "2":
        pass
    elif antPers == "3":
        pass
    elif antPers == "4":
        pass
    elif antPers == "0":
        break
    else:
        print("Det går inte!")

"""



"""
while True:
    print("=" * 30)
    print("VÄLKOMMEN TILL HOTELLET!")
    print("=" * 30)
    print("[1] Checka in")
    print("[2] Checka ut")
    print("[3] Visa boende på hotellet")
    print("[0] Avsluta")
    val = input(": ")

    if val == "1":
        while True:
            print("Skriv hur många besökare som checkar in.")
            antPers = input(": ")
            if antPers == "1":
                pass
            elif antPers == "2":
                pass
            elif antPers == "3":
                pass
            elif antPers == "4":
                pass
            elif antPers == "0":
                break
            else:
                print("Det går inte!")

    elif val == "2":
        pass
    elif val == "3":
        pass
    elif val == "0":
        break
    else:
        print("Det går inte!")
        """


root = Tk()
Main(root)
root.mainloop()
