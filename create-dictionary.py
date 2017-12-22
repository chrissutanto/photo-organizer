import os, hashlib

# writes new text file called "dictionary
dictionary = open("dictionary.txt", "w")


def parse_directory(directory):
    """goes through current directory and subdirectories, calling writeToDictionary on all files"""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            write_to_dictionary(os.path.join(root, filename))


def write_to_dictionary(location):
    """writes to dictionary current item name and SHA1 hash"""
    hash = hashlib.sha1()
    bufferSize = 65536
    with open(location, 'rb') as file:
        buffer = file.read(bufferSize)
        while len(buffer) > 0:
            hash.update(buffer)
            buffer = file.read(bufferSize)
    dictionary.write(os.path.relpath(location, startDir) + " : " + str(hash.hexdigest()) + "\n")


print("enter directory")
startDir = str(input())
#startDir = 'C:/Users/chris/Documents/Python Projects/Test/testfldr'  # placeholder directory
parse_directory(startDir)
print("written to dictionary.txt")
