#Nick Hardy Assignment 10.1 Working with Files CIS245-T303

import os

dir_loc = input("Please enter location of directory: ")

file_name = input("Please enter the file name: ")

if not os.path.isdir(dir_loc):

    os.makedirs(dir_loc)

    print("folder created")

full_path = dir_loc + file_name

file_1 = open(full_path, 'a')

name = input("Enter the name: ")
file_1.write(name + ',') 

address = input("Enter the address: ")
file_1.write(address + ',')

phone_num = input("Enter the phone number: ")
file_1.write(phone_num)
file_1.close() 

file_2 = open(full_path, 'r')
output = file_2.readlines()

print(output)

file_2.close()

