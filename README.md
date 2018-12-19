# Project: complete
# Twicth Steamer

ค้นหาเกมส์และสตรีมเมอร์ที่คนนิยมเข้าชม 
โดยอ้างอิงจาก API ของ Twitch และนำมา 
วิเคราะห์ด้วยโปรแกรมต่างๆ แล้วจึงนำมาสร้างกราฟ 
เพื่อเปรียบเทียบข้อมูลในแต่ละส่วน

# Web Twitch Analyza
http://www.it.kmitl.ac.th/~it61070149/psitproject/Home.html
# วิดีโอนำเสนอ
https://www.youtube.com/watch?v=4kQusq1jlII&feature=youtu.be

# สมาชิก
 61070101 นางสาวนวพร  จรัสตระกูล <br /> 
 61070149 นายพีรวิชญ์ สาแก้ว <br />
 61070174 นายภูวิศ  เชื้อชม <br />
 61070180 นายรพิรัตน์ แป้นบูชา <br />

# เราทำอะไร
Project นี้จัดทำขึ้นเพื่อวิเคราะห์ตรวจสอบและค้นหาเกมส์และเหล่าสตรีมเมอร์ชื่อดังทั่วโลกหลากหลายประเทศที่คนนิยมเข้าชม โดยอ้างอิงจาก API ของ Twitch และนำมา วิเคราะห์ด้วยภาษาPython และโปรแกรมต่างๆ เพื่อเปรียบเทียบข้อมูลในแต่ละส่วน จากนั้นจึงนำมาวิเคราะห์เพื่อหาข้อสรุป 3 อย่างคือ <br /> 
 1.สตรีมเมอร์นิยมสตรีมเกมอะไร <br /> 
 2.คนดูสนใจดูเกมอะไร <br /> 
 3.เวลาไหนที่คนนิยมดูการถ่ายทอดสดมากที่สุด <br /> 
 เมื่อได้ข้อสรุปทั้งหมดแล้ว เราก็จะเอาข้อสรุปทั้งหมดมานำเสนอในรูปแบบกราฟและนำเสนอผ่านเว็ปไซต์ต่อไป

# ข้อมูลที่ใช้ในการวิเคาระห์
ข้อมูลการสตีมมิ่งของuserต่างๆตั้งแต่วันที่ 6 ธันวาคม 2561 ถึง 13 ธันวาคม 2561 ในช่วงเวลาตั้งแต่ 09.00น.-00.00น.

# ผลการดำเนินการ
จากการวิเคาระห์ข้อมูลเพื่อหาข้อสรุปจากที่ได้กล่าวในเป้าหมายของ Project นี้ สรุปได้ว่า
1. สตรีมเมอร์นิมยมสตรีมเกม Fortnite มากที่สุด โดยมีจำนวนการสตรีมทั้งหมด 4665 ครั้ง รองลงมาคือ Just Chatting <br />
ที่มีจำนวนการสตรีม 3388 ครั้ง และ League of Legends ที่มีจำนวนการสตรีม 	3136 ครั้ง ตามลำดับ <br />
2. เกมที่ผู้ชมสนใจรับชมมากที่สุดคือ Fortnite โดยมีจำนวนยอดผู้ชมรวม 2,662,354 คน รองลงมาคือ League of Legends <br />
ที่มียอดผู้ชมรวม 2,080,511 คน และ Super Smash Bros. Ultimate ที่มียอดผู้ชมรวม 	1,318,158 คน ตามลำดับ
3. ช่วงเวลาที่ผู้ชมนิยมรับชมมากที่สุดคือ ช่วง 09.00น.-12.00น. โดยมีจำนวนยอดผู้ชมรวม 5,912,723 คน รองลงมาคือช่วง 21.01น.-00.00น ที่มียอดผู้ชมรวม 5,083,513 คน และช่วง 18.01น.-21.00น ที่มียอดผู้ชมรวม 2,710,123 ตามลำดับ 


# Modules
python-twitch-client
https://python-twitch-client.readthedocs.io/en/latest/<br />
csv
https://docs.python.org/3/library/csv.html
