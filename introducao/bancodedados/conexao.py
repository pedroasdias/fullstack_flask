import pymysql
hostname = 'database1.c3awyky0axj2.us-west-2.rds.amazonaws.com'
user = 'admin'
passoword = 'admin3311'

db = pymysql.connections.Connection(
    host=hostname,
    user=user,
    password=passoword
)

#teste

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS notebooks_db_pedro_augusto")
cursor.execute("SHOW DATABASES")

for databases in cursor:
    print(databases)

cursor.close()
db.close()

