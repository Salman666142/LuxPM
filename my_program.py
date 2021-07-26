import json
from io import StringIO
import mysql as mysql
from mysql import connector
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_data():
    counter = 0
    first_number = 0
    odd_list = []
    while counter < 20:
        if first_number % 2 != 0:
            odd_list.append(first_number)
            counter += 1
        first_number += 1
    odd_list = odd_list[::-1]
    eight_odd_numbers = odd_list[:8]

    my_letters = "luxPMsoft"
    json_string = []
    json_string += my_letters[0]
    my_letters = my_letters[1:]
    for i in range(0, len(my_letters)):
        json_string.append(eight_odd_numbers[i])
        json_string += my_letters[i]

    my_json_string = json.dumps(json_string)
    return my_json_string


@app.route('/<encoded_string>', methods=["PUT"])
def inserting_data(encoded_string):
    if str(isinstance(encoded_string, list)) == "True":
        insert_values = tuple(encoded_string)
    else:
        my_string = StringIO(encoded_string)
        insert_values = tuple(json.load(my_string))

    my_db = mysql.connector.connect(user='SalmanFaris', password='S9634765J',
                                    host='127.0.0.1',
                                    database='Faris')

    cursor = my_db.cursor()

    insert_query = "insert into Faris.results (starting_value , second_value , third_value , fourth_value , " \
                   "fifth_value ,sixth_value , seventh_value ,eighth_value , ninth_value, tenth_value , " \
                   "eleventh_value , twelfth_value , thirteenth_value ,fourteenth_value ,fifteenth_value , " \
                   "sixteenth_value ,seventeenth_value) Values (%s, %s,%s, %s,%s, %s,%s, " \
                   "%s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"

    cursor.execute(insert_query, insert_values)
    my_db.commit()
    result = "Row added"
    my_db.close()
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5000)
