import json
import sqlite3
from flask import Flask
app = Flask(__name__)

con = sqlite3.connect('animal.db')
cursor = con.cursor()
cursor.execute('DROP TABLE colors')
con.commit()
query_2 = "CREATE TABLE colors(Id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR (30) UNIQUE)"
cursor.execute(query_2)
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
# cursor.execute('DELETE FROM colors')
# con.commit()
query_2 = "INSERT INTO colors (name) SELECT DISTINCT color1 FROM animals"
cursor.execute(query_2)
con.commit()
con.close()


connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
query = "CREATE TABLE animal_colors(animal_id INTEGER, color_id INTEGER)"
cursor.execute(query_2)
connection.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
cursor.execute('DELETE FROM animal_colors')
con.commit()
query_2 = 'INSERT INTO animal_colors SELECT animals."index", colors.id FROM animals JOIN colors ON color1 = colors.name'
cursor.execute(query_2)
con.commit()
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = 'INSERT INTO animal_colors SELECT animals."index", colors.id FROM animals JOIN colors ON color2 = colors.name'
cursor.execute(query_2)
con.commit()
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = "CREATE TABLE outcomes(outcomes_id INTEGER PRIMARY KEY AUTOINCREMENT," \
           "outcome_subtype VARCHAR (50)," \
           "outcome_type VARCHAR (30)," \
           "outcome_month INT," \
           "outcome_year INT)"
cursor.execute(query_2)
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = 'INSERT INTO outcomes (outcome_subtype, outcome_type, outcome_month, outcome_year)' \
          'SELECT outcome_subtype, outcome_type, outcome_month, outcome_year FROM animals GROUP BY outcome_subtype,' \
          'outcome_type, outcome_month, outcome_year, outcome_type, outcome_month, outcome_year'
cursor.execute(query_2)
con.commit()
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = "CREATE TABLE animal_types(ID INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30))"
cursor.execute(query_2)
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = 'INSERT INTO animal_types (name) SELECT DISTINCT (animal_type) FROM animals'
cursor.execute(query_2)
con.commit()
con.close()


connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
query_2 = "CREATE TABLE breed(ID INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30))"
cursor.execute(query_2)
connection.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = 'INSERT INTO breed (name) SELECT DISTINCT (breed) FROM animals'
cursor.execute(query_2)
con.commit()
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = "CREATE TABLE animals_fin (id INTEGER PRIMARY KEY AUTOINCREMENT," \
           "age_upon_outcome VARCHAR (30)," \
           "animal_id VARCHAR (30)," \
           "type_id INT," \
           "name VARCHAR (50)," \
           "breed_id INT," \
           "date_of_birth DATA," \
           "outcome_id INT)"
cursor.execute(query_2)
con.close()


con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_2 = 'INSERT INTO animals_fin SELECT "index", age_upon_outcome, animal_id, animal_types.ID, animals.name, ' \
          'breed.ID, date_of_birth, outcomes.outcomes_id FROM animals '  \
          'LEFT JOIN animal_types ON animal_type = animal_types.name ' \
          'LEFT JOIN breed ON animals.breed = breed.name ' \
          'LEFT JOIN outcomes ON animals.outcome_subtype = outcomes.outcome_subtype ' \
          'AND animals.outcome_type = outcomes.outcome_type ' \
          'AND animals.outcome_month = outcomes.outcome_month ' \
          'AND animals.outcome_year = outcomes.outcome_year'
cursor.execute(query_2)
con.commit()
con.close()


if __name__ == '__maine__':
    app.run()