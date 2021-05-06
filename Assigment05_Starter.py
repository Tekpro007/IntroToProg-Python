# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kyle Gilpin, 5.4.2021, Added code for showing current item
# Kyle Gilpin, 5.5.2021, Add code for adding, removing, saving, and exiting the program
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" #A string that stores the task from a user input
strPriority = "" #A String to that stores the priority from the user input



# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        strData =open(objFile, "r")
        for row in strData:
            lstTable = row.split(",")
            dicRow = {"Task": lstTable[0], "Priority": lstTable[1]}
            print('Task = ' + dicRow["Task"] + " | " + 'Priority = ' + dicRow["Priority"].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask=input("Enter Task: ")
        strPriority=input("Enter Priority: ")
        dicRow = {"Task": strTask, "Priority":strPriority}
        print("Data saved to memory.  Use option 4 to save to hard drive.")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        dicRow = {}
        print("Memory cleared.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file1
    elif (strChoice.strip() == '4'):
        strData = open(objFile, "a")
        strData.write(dicRow["Task"]+ "," + dicRow["Priority"] + '\n')
        strData.close()
        print("Saved Data.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting Program.")
        break  # and Exit the program
