import psycopg2
con = psycopg2.connect(host='database-1.cehgg8mvfi3e.us-east-1.rds.amazonaws.com',database='postgres', user='postgres',password='1234567890')


con.autocommit = True
cur = con.cursor()
cur.execute('create database inventario;')
con.commit()

con.close()
