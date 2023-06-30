import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])

#This will help you understand the structure of the code.
#You can view the exact format in json via: https://jsonviewer.stack.hu/
#print(response.json())


#From the print, our interest is in the trackName names, then we can 
#loop through the results and print the results

resultCount = response.json()
for objects in resultCount["results"]:
    print(objects["trackName"])
