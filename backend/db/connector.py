import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             port=8889,
                             database='roomie_mine',
                             cursorclass=pymysql.cursors.DictCursor)
