#!/usr/bin/python3
import MySQLdb
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "raspberry", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # execute SQL query
        cursor.execute("SELECT VERSION();")
        # Fetch a single row
        data = cursor.fetchone()
        print("Database version : %s " % data)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

