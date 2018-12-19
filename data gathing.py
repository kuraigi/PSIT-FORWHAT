from twitch import TwitchHelix
import csv

client = TwitchHelix(client_id='w2fwifqxprja6cvm1i251tyqbgd1ot')
streams_iterator = client.get_streams(page_size=10)


with open('filename.csv', 'w', newline='',encoding="utf-8") as csvfile:
    fieldnames = ['user_name','language', 'game_id', 'game_name', 'start_time(UTC Time)', 'view_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for stream in streams_iterator:
         game_top = client.get_games(game_ids=[stream['game_id']])

         for name in game_top:
              writer.writerow({'user_name':stream["user_name"],'language': stream["language"], 'game_id':stream["game_id"], 'game_name': name['name'], 'start_time(UTC Time)': stream["started_at"], 'view_count': stream["viewer_count"]})
              
   

