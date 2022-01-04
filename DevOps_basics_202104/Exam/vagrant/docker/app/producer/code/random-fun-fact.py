import mysql.connector
import random

a = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Fat', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong', 'Slim']
d = ['Eat', 'Dream', 'Like', 'Adore', 'Trow', 'Love', 'Dislike']
e = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

s = a[random.randrange(10)] + " " + b[random.randrange(11)] + " Are " + c[random.randrange(7)] + " And " + d[random.randrange(6)] + " " + e[random.randrange(6)]

print("New fun fact discovered: " + s)

try:
  mydb = mysql.connector.connect(
    host="dob-storage",
    user="root",
    password="Exam-2021",
    database="animal_facts"
  )
  cursor = mydb.cursor()
  cursor.execute("INSERT INTO facts (fact) VALUES ('" + s + "')")
  cursor.close()
  mydb.commit()
except:
  print("ERROR: Database communication error.")
