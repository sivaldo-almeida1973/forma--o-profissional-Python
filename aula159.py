import psycopg2
con = psycopg2.connect(host='database-1.cehgg8mvfi3e.us-east-1.rds.amazonaws.com',database='inventario', user='postgres',password='1234567890')


con.autocommit = True
cur = con.cursor()
cur.execute("select * from arquivos")
recset = cur.fetchall()
for rec in recset:
  print(rec)

con.close()
