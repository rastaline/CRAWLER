import json
file= open('BOOKS.txt','a+')
with open('BOOKS.json','r') as json_file:
    for line in json_file.readlines():
        data= json.loads(line.strip())
        for item in data:
            file.write(item)    
            print(item)