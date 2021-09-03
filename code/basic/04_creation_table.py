#!/usr/bin/python3
import MySQLdb
# MySQLdb.connect(host,user,password,dbname)
db = MySQLdb.connect("192.168.X.XXX", "root", "raspberry", "")
def main():
        # prepare a cursor object
        cursor = db.cursor()
        # Drop database if already exist
        cursor.execute("DROP TABLE IF EXISTS app_db.user;")
        # Create table as per requirement
        query = """
                CREATE TABLE IF NOT EXISTS app_db.user(
                        id INT(16) NOT NULL AUTO_INCREMENT,
                        user_name VARCHAR(32)  NOT NULL UNIQUE,
                        user_pass VARCHAR(32)  NOT NULL,
                        user_privilege INT(4)  NOT NULL,
                        user_status INT(4)  NOT NULL,
                        user_time_created DATETIME(6)  NOT NULL,
                        user_time_modified DATETIME(6)  NOT NULL,
                        PRIMARY KEY (`id`)
                );
                """
        cursor.execute(query)
        print("table successfully created")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
finally:
        db.close()

