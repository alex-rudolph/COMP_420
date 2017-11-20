import datetime
import mysql.connector
from mysql.connector import errorcode

## connect to database with error checking

# try:
dbCnctn = mysql.connector.connect(user='root', password='Fimbulvetr96',
                                host='localhost',
                                database='AVIATIONCO')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   dbCnctn.close()
## Execute DB queries
## used to execute query
cursor = dbCnctn.cursor()

query1 = ("SELECT CUS_CODE FROM customer")

cursor.execute(query1)

for(CUS_CODE) in cursor:
    print("{}".format(CUS_CODE))

cursor.close()
