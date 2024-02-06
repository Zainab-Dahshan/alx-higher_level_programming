def read_file(filename=""):
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a valid file name.")

# Example usage:
# read_file('example.txt')
