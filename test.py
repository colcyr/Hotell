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

def addToTxt():
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

def addToInfo(name, age, number):
    """
    Method for writing to the list containing all the guests 

    args:
        name (string): A string with the name of the person that is supposed to be written in
        age (string): A variable containing the users age, not an int as it is not supposed to be counted or used in calculations
        number (string): Same as age just the phone number of the user
    """
    t = open("testinfo.txt", "a")
    t.write("\nGuest")
    t.write("\nName: " + name)
    t.write("\nAge: " + age)
    t.write("\nNumber: " + number)
    t.close()

def roomInput(v):
    for x in range(0, 4): #Runs through the available rooms of the kind and if it detects an available it changes then breaks the for loop
        if v[x].name == "Available":
            v[x].name = "Taken(" + Q2 + ")"
            break
    else:
        print("Alla rum av denna typ är tagna")

def writeFromDoc(p):
    #prints all rooms
    t = open(p, "r")
    i = t.readlines() #reads all the lines into i which is a list
    for x in i: #prints the lines one after another
        print(x)
    t.close()
#start of actual program

"""
Vill du lägga in en bokning
    lägga in
    boka fler rum
Vill du ta bort en bokning
    På ett rum eller alla 
Se över alla rum eller alla som har bokat ett
"""
while True:
    addToProgram()
    print("\nMake our choice: \n1. Lägga in en bokning \n2. Ta bort en bokning \n3. Se över alla bokningar \n0. Avsluta")
    start_quest = input(":: ")

    if start_quest == "1":
        Q2 = input("What is your firstname: ").lower()
        Qage = input("How old are you: ")
        Qnumber = input("What is your phonenumber: ")
        addToInfo(Q2, Qage, Qnumber)
        while True:
            Q1 = input("What kind of room do you want: ")
            

            if Q1 == "1":
                #Runs through the available rooms of the kind and if it detects an available it changes then breaks the for loop
                #rooms1
                roomInput(list_1room)
            elif Q1 == "2":
                #rooms2
                roomInput(list_2room)
            elif Q1 == "3":
                #rooms3
                roomInput(list_3room)
            elif Q1 == "4":        
                #rooms4
                roomInput(list_4room)
            else:
                print("Not recognized number of rooms")
            #Runs after the loops 
            Q3 = input("Do you want to add any more rooms (Yes/No): ").lower()
            if Q3 == "yes":
                pass
            elif Q3 == "no":
                addToTxt()
                #breaks the while loop
                break
            else:
                print("You need to answer yes or no")


    elif start_quest == "2":
        Q_remove = input("1. Ta bort ett rum\n2. Ta bort alla rum\nHur många rum vill du ta bort: ") #choose if you want to remove one room or all rooms tied to a person
        nameSearch = input("Vad är ditt namn: ").lower()
        if Q_remove == "1":
            Q_whichRoom = int(input("Vilken sorts rum vill du ta bort: "))
            y = Q_whichRoom - 1
            for x in all_rooms[y]:
                if nameSearch in x.name:
                    x.name = "Available"
                    addToTxt()
                    break
                else:
                    pass
        elif Q_remove == "2":
            for x in range(0, 3):
                for i in all_rooms[x]:
                    if nameSearch in i.name:
                        i.name = "Available"
                    else:
                        pass
            addToTxt()
            
        else:
            print("Du måste skriva in 1 eller 2")
    elif start_quest == "3":
        Q_what = input("1. Skriv ut alla rum \n2. Skriv ut alla användare \nSkriv vilket nummer du väljer: ")
        if Q_what == "1":
            #prints all rooms
            writeFromDoc("test.txt")
        elif Q_what == "2":
            #prints all users
            writeFromDoc("testinfo.txt")
        else:
            print("Du måste skriva 1 eller 2")
        
    elif start_quest == "0":
        """
        make it look nice 
        """
        print("Shutting down")  
        break
    else: print("Unknown input")