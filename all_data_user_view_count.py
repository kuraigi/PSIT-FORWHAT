import csv

with open('all_data.csv', encoding="ISO-8859-1")as file:
    reader = csv.DictReader(file)
    dct = {}
    lst = []

    
    for row in reader:
        key = row['user_name'],row["language"]
        dct[key] = dct.get(key, 0) + int(row['view_count'])
         
with open('all data user view_count.csv', 'w', newline='',encoding="utf-8") as csvfile:
    fieldnames = ['user_name','language', 'total view_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for name in dct:
        writer.writerow({'user_name':name[0],'language': name[1] , 'total view_count':dct[name]})
         
                

