import json
import sqlite3
from flask import Flask
app = Flask(__name__)


@app.route('/<int:id>')
def animal_data(id):
    con = sqlite3.connect('animal.db')
    cursor = con.cursor()
    sql = 'SELECT age_upon_outcome, animal_id, animal_types.name, breed.name, date_of_birth FROM animals_fin ' \
          'LEFT JOIN breed on animals_fin.breed_id = breed.ID ' \
          f'LEFT JOIN animal_types on animals_fin.type_id = animal_types.id WHERE animals_fin.id = {id}'
    cursor.execute(sql)
    result = cursor.fetchall()
    con.close()
    print(f'result={result}')
    result_dict = {
        "age_upon_outcome": result[0][0],
        "animal_id": result[0][1],
        "animal_type": result[0][2],
        "breed": result[0][3],
        "date_of_birth": result[0][4],
        }
    return json.dumps(result_dict)


if __name__ == '__main__':
    app.run()
