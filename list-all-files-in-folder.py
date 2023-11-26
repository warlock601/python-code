import os

user_input=input("Provide all the folder names :")
list_user_input=list(map(str,user_input.split()))                 # input from user map it in the form a list

for folders in list_user_input:
    try:                                                          # what if the user provided wrong folder name, for this we have exception handling
        files=os.listdir(folders)
    except FileNotFoundError:
        print("Please enter a valid folder name for this folder: " + folders)      #
        continue
    print("-----Files present in the folder " + folders + " are :")
    for file in files:
        print(file) 
   
