# prog to print the usernames and pull requests that a user has created

import requests

url=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if url.status_code==200:    
    response=url.json()                 # convert the json response into a dictionary
    
    pull_creators={}

    for pull in response:
        creator=pull["user"]["login"]
        if creator in pull_creators:                # means if the creator is already in the dict, then increment otherwise equal to 1
            pull_creators[creator]+=1               
        else:
            pull_creators[creator]=1    

    for i,count in pull_creators.items():
        print(f"{i} : {count} PRs")                 # just as we use %d in c language to print to print a variable value, here we use f"{}"

else:
    print("Unable to fetch the data with status code: " + str(url.status_code))

