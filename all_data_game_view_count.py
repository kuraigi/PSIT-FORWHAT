import csv

with open('all_data.csv', encoding="ISO-8859-1")as file:
    reader = csv.DictReader(file)
    dct = {}
    lst = []

    
    for row in reader:
         dct[row['game_name']] = dct.get(row['game_name'], 0) + int(row['view_count'])
         
with open('all data game view_count.csv', 'w', newline='',encoding="utf-8") as csvfile:
    fieldnames = ['game_name', 'total view_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for name in dct:
        writer.writerow({'game_name':name , 'total view_count':dct[name]})
         
                

