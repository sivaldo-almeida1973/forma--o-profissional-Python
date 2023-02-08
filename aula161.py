import boto3
import io
from io import BytesIO
import psycopg2

s3 = boto3.resource(
  service_name = 's3',
  region_name ='sa-east-1',
  aws_access_key_id = 'AKIAYA3EVBTEUBHTFB7K', 
  aws_secret_access_key = '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'

)
bucket = 'sivaldoaulapython'
prefix = 'imagens/'


con = psycopg2.connect(host='database-1.cehgg8mvfi3e.us-east-1.rds.amazonaws.com',database='inventario', user='postgres',password='1234567890')
con.autocommit = True
id = 1


for object_s3 in s3.Bucket(bucket).objects.filter(Prefix = prefix):
  if object_s3.key.endswith('png') or object_s3.key.endswith('PNG'):
    #print(object_s3)
    filename = object_s3.key.split('/')[1]
    cur = con.cursor()
    cur.execute("insert into arquivos (idarquivo, nomearquivo) values (%d,' %s')" %(id, filename))
    id += 1


con.close()
