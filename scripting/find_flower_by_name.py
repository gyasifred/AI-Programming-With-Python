#!/usr/bin/python3
def flower_dictionary(file: str):
    flower_dic = {}
    with open(file=file, mode='r') as fh:
        for line in fh:
            tmp = line.strip()
            if tmp:
                flower_dic[tmp.split(':')[0].upper()] = tmp.split(":")[
                                     1].strip()
    return flower_dic


if __name__ == '__main__':
    flower_dict = flower_dictionary("flowers.txt")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")

    first_letter = first_name[0].upper()
    if first_letter in flower_dict:
        flower_name = flower_dict[first_letter]
        print("Unique flower name with the first letter:", flower_name)
    else:
        print("Sorry, no flower found with the same first letter as your first name.")
