#!/usr/bin/python3
import MySQLdb
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "raspberry", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # Drop database if already exist
        cursor.execute("DROP DATABASE IF EXISTS app_db;")
        # Create database as per requirement
        cursor.execute("CREATE DATABASE IF NOT EXISTS app_db;")
        print("database successfully created!")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

