import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  with open('app.tpl') as f:
    template = f.read()

  facts = ""

  mydb = mysql.connector.connect(
    host="dob-storage",
    user="root",
    password="Exam-2021",
    database="animal_facts"
  )
  cursor = mydb.cursor()

  cursor.execute("SELECT CONCAT('<li>', fact, '</li>') html_fact FROM facts ORDER BY id DESC LIMIT 10")

  records = cursor.fetchall()

  for row in records:
    facts = facts + row[0]

  cursor.close()

  result = template.replace("{FACTS}", facts)

  with open('app.dat') as f:
    build = f.read()

  result = result.replace("{BUILD}", build)

  return result