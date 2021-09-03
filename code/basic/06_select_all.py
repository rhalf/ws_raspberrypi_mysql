#!/usr/bin/python3
import MySQLdb
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "raspberry", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # Select rows from the table
        cursor.execute("SELECT * FROM app_db.user;")
        # show all rows 
        rows = cursor.fetchall()
        for row in rows:
                print(row)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

