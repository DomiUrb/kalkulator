import pymysql as mysql
#import MySQLdb as sqldb


con = mysql.connect(host='localhost', user='admin', passwd='asd545!', db='klienci')

cur = con.cursor() # mozna wysalc zapytaie do bazy

cur.execute('USE database_name')
cur.execute('SHOW TABLES')

for record in cur:
    print(record[0])

cur.close()
