#Customizable Bot
import os
from os.path import exists

fileNames = ["name", "sex", "hobby"]

SetupAlreadyDone = False

ExistsNeed = exists (fileNames[0])
if ExistsNeed == False:
    with open(fileNames[0], "w") as file:
        file.write("")
    with open(fileNames[1], "w") as file:
        file.write("")
    with open(fileNames[2], "w") as file:
        file.write("")
    

with open(fileNames[2], "r") as file:
    content = file.read()
    if content != "":
        SetupAlreadyDone = True

Error = False
Name = ""
Hobby = ""

print("Starting Up...")

if SetupAlreadyDone == True:
    Hobby = content
    with open(fileNames[1], "r") as file:
        content = file.read()
    MaleFemale = content
    with open(fileNames[0], "r") as file:
        content = file.read()
    Name = content
    #print (f"Name: {Name}\nSex: {MaleFemale}\nHobby: {Hobby}")
elif SetupAlreadyDone == False:
    print("To use this bot, you must finish customizing it.\n")

    MaleFemale = input("What is the sex for your bot? Male or Female?\n")

    if MaleFemale == "male" or MaleFemale == "Male" or MaleFemale == "female" or MaleFemale == "Female":
        print(f"Your bot is a {MaleFemale}\n")
    elif 1 < 2:
        print(f"Error! Expected either 'male' or 'female' but got {MaleFemale}")
        Error = True

    if Error == False:
        Name = input("What is the name of your bot?\n")
        if Name != "":
            print("")
        elif Name == "":
            print("Error! Expected a value but got nothing.")
            Error = True
    if Error == False:
        Hobby = input(f"What is {Name}'s favorite hobby?\n")
        if Hobby != "":
            with open(fileNames[0], "w") as file:
                file.write(Name)
            with open(fileNames[1], "w") as file:
                file.write(MaleFemale)
            with open(fileNames[2], "w") as file:
                file.write(Hobby)
        elif Hobby == "":
            print("Error! Expected a value but got nothing.")
            Error = True

if Error == False:
    print(f"{Name} is ready.")
            