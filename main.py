import os

def createFile(file_name):
    with open(file_name, 'w') as f:
        f.write("Hello World!")
    print("File created successfully!")
    return

def readFile(file_name):
    with open(file_name, 'r') as f:
        print(f.read())

def updateFile(file_name, content):
    with open(file_name, 'a') as f:
        f.write(f"\n{content}")
        print("File updated successfully!")

def deleteFile(file_name):
    try:
        os.remove(file_name)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to delete file!")

def main():
    while True:
        print("\nPress 1 for creation of a file.")
        print("Press 2 for reading a file.")
        print("Press 3 for updating of a file.")
        print("Press 4 for deletion of a file.")
        print("Press 5 to exit.")
        
        try:
            req = int(input("Enter your choice: "))
            
            if req == 5:
                print("Exiting program...")
                break
                
            if req == 1:
                print("You have chosen to create a file.")
                file_name = input("Enter the name of the file: ")
                createFile(file_name)
                
            elif req == 2:
                print("You have chosen to read a file.")
                file_name = input("Enter the name of the file: ")
                readFile(file_name)
                
            elif req == 3:
                print("You have chosen to update a file.")
                file_name = input("Enter the name of the file: ")
                content = input("Enter content to add: ")
                updateFile(file_name, content)
                
            elif req == 4:
                print("You have chosen to delete a file.")
                file_name = input("Enter the name of the file: ")
                deleteFile(file_name)
                
            else:
                print("Invalid choice! Please select a number between 1 and 5.")
                
        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
