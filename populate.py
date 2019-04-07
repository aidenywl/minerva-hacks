import mysql.connector

my_db = None
my_cursor = None

my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="minerva"
    )

my_cursor = my_db.cursor()

github_data = \
[-122.39116,37.78242,
-122.38981,37.78135,
-122.38976,37.7813,
-122.38982,37.78125,
-122.38998,37.78113,
-122.39017,37.78097,
-122.39037,37.78081,
-122.39044,37.78076,
-122.39054,37.78068,
-122.3906,37.78073,
-122.39079,37.78088,
-122.39168,37.78158,
-122.39202,37.78186,
-122.3913,37.78244]

la = []
lo = []

for index, elem in enumerate(github_data):
    if index % 2 == 0:
        la.append(elem)
    else:
        lo.append(elem)

client_id = 123456789
latitude = None
longitude = None
unix_time = 0

for index, elem in enumerate(la):
    add_interceptor_command = "INSERT INTO geodata (client_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s)"
    add_interceptor_command_variables = (client_id, lo[index], elem, unix_time)
    my_cursor.execute(add_interceptor_command, add_interceptor_command_variables)
    my_db.commit()
    unix_time += 1

# ---------------------------------------------------------intercepts---------------------------------------------------------------------
latitude_list = [30.3358376, 30.307977, 30.3216419]
longitude_list = [77.8701919, 78.048457, 78.0413095]
interceptor_ids = [987654321, 908765432, 876543210]

for index, elem in enumerate(latitude_list):
    add_interceptor_command = "INSERT INTO intercepts (client_id, interceptor_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s, %s)"
    add_interceptor_command_variables = (client_id, interceptor_ids[index], elem, longitude_list[index], unix_time)
    my_cursor.execute(add_interceptor_command, add_interceptor_command_variables)
    my_db.commit()
    unix_time += 1
