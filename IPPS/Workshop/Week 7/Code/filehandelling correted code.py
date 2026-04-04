input_file_opened = False
while not input_file_opened:
    try:
        file_name = input("Enter file name: ")
        with open(file_name,"r") as input_file:
            input_file_opened = True
    except FileNotFoundError:
        print("Input file not found")
    except PermissionError:
        print("No permission to open the file")
        
        
