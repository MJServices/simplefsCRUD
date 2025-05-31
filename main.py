print("Press 1 for creation of a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating of a file.")
print("Press 4 for deletion of a file.")

try:
    req = int(input("Enter your choice: "))
    if req == 1:
        print("You have chosen to create a file.")
        try:
            file_name = input("Enter the name of the file: ")
            createFile(file_name)
        except:
            print("Invalid Input!")
            exit()

        if req == 2:
            print("You have chosen to read a file.")
        try:
            file_name = input("Enter the name of the file: ")
            readFile(file_name)
        except Exception as e:
            print(f"Error occured {e}")
            exit()

        if req == 3:
            print("You have chosen to update a file.")
        try:
            file_name = input("Enter the name of the file: ")
            updateFile(file_name)
        except Exception as e:
            print(f"Error occured {e}")
            exit()
        if req == 4:
            print("You have chosen to delete a file.")
        try:
            file_name = input("Enter the name of the file: ")
            deleteFile(file_name)
        except Exception as e:
            print(f"Error occured {e}")
            exit()
except Exception as e:
        print(f"Error occured {e}")
        exit()

def createFile(file_name):
    pass

def readFile(file_name):
    pass

def updateFile(file_name):
    pass

def deleteFile(file_name):
    pass