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

    average_latitude = 0
    average_longitude = 0

    for intercept in intercepts:
        latitude_list.append(float(intercept[3]))
        longitude_list.append(float(intercept[4]))
        average_latitude += float(intercept[3])
        average_longitude += float(intercept[4])

    average_latitude = average_latitude/len(latitude_list)
    average_longitude = average_longitude/len(longitude_list)

    google_map = gmplot.GoogleMapPlotter(average_latitude, average_longitude, 13)
    google_map.apikey = api_key

    google_map.scatter(latitude_list, longitude_list, '#FF0000', size=100, marker=True)

    google_map.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=2.5)

    google_map.draw(html_file)
    os.system("open " + html_file)


if __name__ == '__main__':
    client_id = sys.argv[1]
    main()
