import shutil, os



def sort_dictionary(dictionary):
    """sorts list based on hash"""
    dictionary_lines = dictionary.readlines()
    dictionary_list = []  # list of tuples where first value is hash, second value is filename
    for line in dictionary_lines:
        filename, hash_value = line.split(' : ')
        hash_value = hash_value[:-1]
        dictionary_list.append((hash_value, filename))
    return sorted(dictionary_list)


def find_duplicates(list):
    """if a hash occurs more than once, write all occurrences onto duplicates.txt"""
    if len(list) != 0 and len(list) != 1:
        curr_item_idx = 0
        next_item_idx = 1
        while next_item_idx < len(list):
            if list[curr_item_idx][0] == list[next_item_idx][0]:
                write_duplicate(list[curr_item_idx])
                write_duplicate(list[next_item_idx])
                curr_item_idx += 1
                next_item_idx += 1
                while list[curr_item_idx][0] == list[next_item_idx][0]:
                    write_duplicate(list[next_item_idx])
                    curr_item_idx += 1
                    next_item_idx += 1
            else:
                curr_item_idx += 1
                next_item_idx += 1


def write_duplicate(item):
    """takes in 2-tuple and writes pair to duplicates.txt in order filename : hash"""
    duplicates.write(str(item[1]) + " : " + str(item[0]) + "\n")


print("enter directory")
startDir = str(input())
dictionary = open(startDir + "/dictionary.txt")
duplicates = open(os.path.join(startDir, "duplicates.txt"), "w")  # file to write duplicates to
sorted_list = sort_dictionary(dictionary)
find_duplicates(sorted_list)
