import dbm
import random
ROSTER = ("Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf")
GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']

db = dbm.open('db_student', 'c')

for student in ROSTER:
    db[student] = '0'
db.close()

def call(base):
    """
    Among the names that are called the least times,
    return one name randomly.

    Update database after each call
    """
    minimum = min(base.values())
    
