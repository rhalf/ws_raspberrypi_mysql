#!/usr/bin/python3
import MySQLdb, sys
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "password", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # Select rows from the table
        query = """
                DELETE FROM app_db.user
                WHERE app_db.user.id = %s;
                """
        param = (sys.argv[1], )
        cursor.execute(query, param)
        db.commit()
        print("item successfully deleted")
        #sudo python3 1
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

