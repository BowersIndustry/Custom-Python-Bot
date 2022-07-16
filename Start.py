#Customizable Bot
import os
from os.path import exists

fileNames = ["name.kyn", "sex.kyn", "hobby.kyn", "customCommands.kyn"]

SetupAlreadyDone = False

command2Start = 3
command3Start = 6
runNewCmd = False
SecondCmd = ""

content = ""

ExistsNeed = exists (fileNames[3])
if ExistsNeed == False:
    with open(fileNames[0], "w") as file:
        file.write("")
    with open(fileNames[1], "w") as file:
        file.write("")
    with open(fileNames[2], "w") as file:
        file.write("")
    with open(fileNames[3], "w") as file:
        file.write("")
    

with open(fileNames[3], "r") as file:
    content = file.read()
    if content != "":
        SetupAlreadyDone = True
    else:
        with open(fileNames[3], "w") as file:
            file.write('print,is a custom command that prints text to the console.,print,Hello World!,run,is a custom command that will run 2 commands at once!,run,print,name,name,is a custom command that will change my name to "New Name",name,New Name')

Error = False
Name = ""
Hobby = ""

print("Starting Up...")

if SetupAlreadyDone == True:
    with open(fileNames[2], "r") as file:
        content = file.read()
    Hobby = content
    with open(fileNames[1], "r") as file:
        content = file.read()
    MaleFemale = content
    with open(fileNames[0], "r") as file:
        content = file.read()
    Name = content
elif SetupAlreadyDone == False:
    print("To use this bot, you must finish customizing it.\n")

    MaleFemale = input("What is the sex for your bot? Male or Female?\n")

    if MaleFemale == "male" or MaleFemale == "female":
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

with open(fileNames[3], "r") as file:
    content = file.read()
    content = content.split(',')
    if content[2] == "print" or content[2] == "name":
        command2Start = 4
    elif content[2] == "run":
        command2Start = 5
    if content[command2Start + 2] == "print" or content[command2Start + 2] == "name":
        command3Start = command2Start + 4
    elif content[command2Start + 2] =="run":
        command3Start = command2Start + 5

if Name == "":
    print("Error! Name is empty.")
    Error = True
if MaleFemale == "female" or MaleFemale == "male":
    MaleFemale = MaleFemale
else:
    print("Error! Sex is not male or female.")
    Error = True
if Hobby == "":
    print("Error! Hobby is empty.")
    Error = True

if Error == False:
    print(f"{Name} is ready.\n")

    while 1 < 2:
        if runNewCmd == False:
            if SecondCmd == "":
                command = input("What do you want me to do? (Use \"help\" for a list of commands!)\n")
            else:
                command = SecondCmd
                SecondCmd = ""
        runNewCmd = False
        if command == "help":
            print(f"\"about\" will give you some details about me.\n\"exit\" will shut me down.\n\"{content[0]}\" {content[1]}\n\"{content[command2Start]}\" {content[command2Start + 1]}\n\"{content[command3Start]}\" {content[command3Start + 1]}\n")
        elif command == "about":
            print(f"\nHello I am {Name}.\nI am a {MaleFemale}.\nMy favorite thing to do is {Hobby}.\n")
        elif command == "exit":
            break
        elif command == content[0]:
            if content[2] == "print":
                print(content[3])
            elif content[2] == "run":
                runNewCmd = True
                command = content[3]
                SecondCmd = content[4]
            elif content[2] == "name":
                Name = content[3]
                with open(fileNames[0], "w") as file:
                    file.write(Name)
            if runNewCmd == False:
                print()
        elif command == content[command2Start]:
            if content[command2Start + 2] == "print":
                print(content[command2Start + 3])
            elif content[command2Start + 2] == "run":
                runNewCmd = True
                command = content[command2Start + 3]
                SecondCmd = content[command2Start + 4]
            elif content[command2Start + 2] == "name":
                Name = content[command2Start + 3]
                with open(fileNames[0], "w") as file:
                    file.write(Name)
            if runNewCmd == False:
                print()
        elif command == content[command3Start]:
            if content[command3Start + 2] == "print":
                print(content[command3Start + 3])
            elif content[command3Start + 2] == "run":
                runNewCmd = True
                command = content[command3Start + 3]
                SecondCmd = content[command3Start + 4]
            elif content[command3Start + 2] == "name":
                Name = content[command3Start + 3]
                with open(fileNames[0], "w") as file:
                    file.write(Name)
            if runNewCmd == False:
                print()
        else:
            print("That is not a valid command.\n")