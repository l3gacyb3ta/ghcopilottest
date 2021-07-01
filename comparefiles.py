import difflib

def get_files() -> list:
    """Gets a list of paths of files the user wants to compare"""
    files = []
    while True:
        file = input("Enter the path of a file to compare (or enter to quit): ")
        if file == "":
            break
        files.append(file)
    return files

def compare(files: list):
    """Compares the files and prints the differences"""
    for file1 in files:
        for file2 in files:
            if file1 != file2:
                print("Comparing", file1, "and", file2)
                with open(file1, "r") as file1_read, open(file2, "r") as file2_read:
                    diff = difflib.unified_diff(file1_read.readlines(), file2_read.readlines())
                    for line in diff:
                        print(line)

compare(get_files())
