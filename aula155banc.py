#Conectando e Interagindocom o Banco de Dados
import psycopg2
con = psycopg2.connect(host='database-1.cehgg8mvfi3e.us-east-1.rds.amazonaws.com',database='postgres', user='postgres',password='1234567890')

cur = con.cursor()

con.close()
