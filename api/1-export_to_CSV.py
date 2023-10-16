#usr/bin/python
import requests
import sys
import csv

id = sys.argv[1]
request = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
request2 = requests.get('https://jsonplaceholder.typicode.com/users/' + id + '/todos')
data = request.json()
data2 = request2.json()
completed = 0
tasks = []

for i in data2:
    if i.get('completed') == True:
        completed = completed + 1
        tasks.append([id, data.get('name'), "Completed", i.get('title')])
    else:
        tasks.append([id, data.get('name'), "Not Completed", i.get('title')])

csv_file = "{}.csv".format(id)

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    #columns
    writer.writerows(tasks)

print(f'Employee {data.get("name")} is done with tasks ({completed}/{len(data2)}):')
for item in data2:
    if item.get('completed') == True:
        print(f'\t {item.get("title")}')

print(f'Data exported to {csv_file}.')