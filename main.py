import os

def createFile(file_name):
    with open(file_name, 'w') as f:
        f.write("Hello World!")
        f.close()
    print("File created successfully!")
    return

def readFile(file_name):
    with open(file_name, 'r') as f:
        print(f.read())
        f.close()

def updateFile(file_name, content):
    with open(file_name, 'a') as f:
        f.write(f"\n{content}")
        print("File updated successfully!")
        f.close()

def deleteFile(file_name):
    try:
        os.remove(file_name)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to delete file!")

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
            exit()
        except Exception as e:
            print(f"Error occured {e}")
            exit()

    if req == 2:
        print("You have chosen to read a file.")
        try:
            file_name = input("Enter the name of the file: ")
            readFile(file_name)
            exit()
        except Exception as e:
            print(f"Error occured {e}")
            exit()

    if req == 3:
        print("You have chosen to update a file.")
        try:
            file_name = input("Enter the name of the file: ")
            content = input("Enter content to add: ")
            updateFile(file_name, content)
            exit()
        except Exception as e:
            print(f"Error occured {e}")
            exit()
    if req == 4:
        print("You have chosen to delete a file.")
        try:
            file_name = input("Enter the name of the file: ")
            deleteFile(file_name)
            exit()
        except Exception as e:
            print(f"Error occured {e}")
            exit()
except Exception as e:
        print(f"Error occured {e}")
        exit()
