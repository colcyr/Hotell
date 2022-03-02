from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    def __init__(self, root):
        root.wm_title("Hotell")
        root.minsize(500, 500)

        HotelName = Label(text="Hotellet", height=5, width=20)
        HotelName.grid(row=1)

        btnCheckIn = Button(text="Checka in", width=20, height=5)
        btnCheckIn.grid(row=2, padx=2, pady=2)

        btnCheckOut = Button(text="Checka ut", width=20, height=5)
        btnCheckOut.grid(row=3, padx=2, pady=2)
        
        btnShow = Button(text="Visa boende", width=20, height=5)
        btnShow.grid(row=4)

        btnQuit = Button(text="Avsluta", width=20, height=5)
        btnQuit.grid(row=5)

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
