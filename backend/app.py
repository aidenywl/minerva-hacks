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


@app.route('/')
def index():
    return 'index'


@app.route('/get_id', methods=['GET'])
def get_id():
    return str(random.randint(100000000, 999999999))


@app.route('/save_location_and_time', methods=['POST'])
def save_location_and_time():
    if request.method == 'POST':
        client_id = request.args.get('client_id')
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        unix_time = request.args.get('unix_time')

        add_geodata_command = "INSERT INTO geodata (client_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s)"
        add_geodata_command_variables = (client_id, latitude, longitude, unix_time)
        my_cursor.execute(add_geodata_command, add_geodata_command_variables)
        my_db.commit()
    else:
        print('Not a POST request')


@app.route('/add_interceptor', methods=['POST'])
def add_interceptor():
    if request.method == 'POST':
        client_id = request.args.get('client_id')
        interceptor_id = request.args.get('interceptor_id')
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        unix_time = request.args.get('unix_time')

        add_interceptor_command = "INSERT INTO intercepts (client_id, interceptor_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s, %s)"
        add_interceptor_command_variables = (client_id, interceptor_id, latitude, longitude, unix_time)
        my_cursor.execute(add_interceptor_command, add_interceptor_command_variables)
        my_db.commit()
    else:
        print('Not a POST request')


if __name__ == '__main__':
    app.run()
