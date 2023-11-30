# opne() is used to open a file, takes 2 parameters-- File path & "r" or "W" for read or Write respectively
# algo for this will be ----    first read the file > write all the contents onto a variable > open the file with write >  change the parameter


def update_file(file_path,key,value):
  with open(file_path,"r") as file:                # Read everything in the given file & created "file" as alias 
    lines=file.readlines()                         # Used readlines() to read each & every line & stored whatever we read in a variable "lines"

  with open(file_path,"w") as file:
    for line in lines:                             # to iterate line by line
      if key in line:
        file.write(key + "=" + value)              # if key is found, replace the value of that key by new value
      else:
        file.write(line)

update_file("serv.conf","MAX_CONNECTIONS","900")
      
