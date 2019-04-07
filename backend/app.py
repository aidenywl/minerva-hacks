from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/location_time', methods=['POST'])
def save_location_and_time():
    if request.method == 'POST':
        id = request.args.get('id')
        location = request.args.get('location')
        time = request.args.get('time')


if __name__ == '__main__':
    app.run()

