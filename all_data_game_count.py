import csv

with open('all_data.csv', encoding="ISO-8859-1")as file:
    reader = csv.DictReader(file)
    dct = {}
    lst = []

    
    for row in reader:
         dct[row['game_name']] = dct.get(row['game_name'], 0) + 1
         
with open('all data game count.csv', 'w', newline='',encoding="utf-8") as csvfile:
    fieldnames = ['game_name', 'steam_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for name in dct:
        writer.writerow({'game_name':name , 'steam_count':dct[name]})
         
                

