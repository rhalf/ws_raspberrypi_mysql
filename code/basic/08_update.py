#!/usr/bin/python3
import MySQLdb, hashlib, time, sys
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "password", "")
def main():
        # prepare a cursor objects
        cursor = db.cursor()
        # Select rows from the table
        query = """
                UPDATE app_db.user
                SET 
                        user_name = %s,
                        user_pass = %s,
                        user_time_modified = %s
                WHERE app_db.user.id = %s;
                """
        uid = sys.argv[1]
        uName, uPass = sys.argv[2], sys.argv[3]
        hashed = hashlib.md5(uPass.encode()).hexdigest()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        param = (uName, hashed, now, uid)
        cursor.execute(query, param)
        db.commit()
        print("Item updated successfully")
        #sudo python3 activity8.py 1 majinboo 654321
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

