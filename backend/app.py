import mysql.connector
from flask import Flask, request
import random

app = Flask(__name__)


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="minerva"
)

my_cursor = my_db.cursor()


def test():
    print('hey there')


@app.route('/')
def index():
    return 'index'


@app.route('/get_id', methods=['GET'])
def generate_id():
    return str(random.randint(100000000, 999999999))


@app.route('/location_time', methods=['POST'])
def save_location_and_time():
    if request.method == 'POST':
        client_id = request.args.get('id')
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        unix_time = request.args.get('time')

        add_data_command = "INSERT INTO geodata (client_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s)"
        add_data_command_variables = (client_id, latitude, longitude, unix_time)
        my_cursor.execute(add_data_command, add_data_command_variables)
        my_db.commit()


if __name__ == '__main__':
    app.run()
