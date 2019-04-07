import sys
import mysql.connector
import gmplot
import os
from IPython import embed


my_db = None
my_cursor = None
client_id = None
html_file = 'map.html'
api_key = 'AIzaSyAer_9aqaqbuEWcdKsjwssdDAd7E71iJlM'


def main():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="minerva"
    )

    my_cursor = my_db.cursor()
    command = """SELECT * FROM intercepts WHERE client_id='%s' ORDER BY unix_time DESC""" % (client_id,)
    my_cursor.execute(command)
    intercepts = my_cursor.fetchall()

    latitude_list = []
    longitude_list = []

    # sum1 = 0;
    # sum2 = 0;
    for intercept in intercepts:
        latitude_list.append(float(intercept[3]))
        longitude_list.append(float(intercept[4]))

    google_map = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 13)
    google_map.apikey = api_key

    google_map.scatter(latitude_list, longitude_list, '#FF0000', size=100, marker=True)

    google_map.draw(html_file)
    os.system("open " + html_file)


if __name__ == '__main__':
    client_id = sys.argv[1]
    main()
