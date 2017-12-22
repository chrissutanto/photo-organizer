import os, hashlib

# writes new text file called "dictionary
dictionary = open("dictionary.txt", "w")

# goes through current directory and subdirectories, calling writeToDictionary on all files
def parseDirectory(directory):
    for root, dirs, files in os.walk(directory):
        print("root " + str(root))
        for filename in files:
            print("file " + str(filename))
            writeToDictionary(os.path.join(root, filename))

# writes to dictionary current item name and SHA1 hash
def writeToDictionary(location):
    hash = hashlib.sha1()
    bufferSize = 65536
    with open(location, 'rb') as file:
        buffer = file.read(bufferSize)
        while len(buffer) > 0:
            hash.update(buffer)
            buffer = file.read(bufferSize)
    print(os.path.relpath(location, startDir) + " : " + str(hash.hexdigest()) + os.linesep)
    dictionary.write(os.path.relpath(location, startDir) + " : " + str(hash.hexdigest()) + os.linesep)


startDir = 'C:/Users/chris/Documents/Python Projects/Test/testfldr'  # placeholder directory
parseDirectory(startDir)
