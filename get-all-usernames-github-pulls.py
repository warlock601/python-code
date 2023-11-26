# to get this, first we need to have "requests" library installed "pip install requests" 
# we'll use this library to get the API requests 
# we can get the github pulls API url from the Github API docs ie /repos/{owner}/{repo}/pulls


import requests
get_url = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")       # owner=kubernetes,repo=kubernetes 

detail=get_url.json()                                                                    # we'll get this in a json format in a variable

for i in range(len(detail)):                                                             # detail[0]- gives first record in dictionary 
    print(detail[i]["user"]["login"])                                                    # detail[0]["id"] - gives the id of the first record in dictionary
                                                                                         # detail[0]["user"]["login"] gives username of first record
