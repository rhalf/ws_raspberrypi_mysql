#!/usr/bin/python3
import MySQLdb
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "password", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # truncate the table
        cursor.execute("TRUNCATE TABLE app_db.user;")
        db.commit()
        print("table truncated successfully")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

