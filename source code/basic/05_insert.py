#!/usr/bin/python3
import MySQLdb, hashlib, time, sys
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "raspberry", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # Create table as per requirement
        query = """
                INSERT INTO 
                app_db.user (
                        user_name, 
                        user_pass, 
                        user_privilege, 
                        user_status, 
                        user_time_created, 
                        user_time_modified)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
        # prepare hash and time
        # uName, uPass = "rhalf", "321321321"
        uName, uPass = sys.argv[1], sys.argv[2]        
        hashed = hashlib.md5(uPass.encode()).hexdigest()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        param = (uName, hashed , "1", "1", now, now)

        cursor.execute(query, param)

        db.commit()
        print("Item inserted successfully")
        #sudo python3 activity5.py rhalf 123456
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()