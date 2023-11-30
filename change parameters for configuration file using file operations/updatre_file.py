def update_file(file_path,key,value):
  with open(file_path,"r") as file:
    lines=file.readlines()

  with open(file_path,"w") as file:
    for line in lines:
      if key in line:
        file.write(key + "=" + value)
      else:
        file.write(line)

update_file("serv.conf","MAX_CONNECTIONS","900")
      
