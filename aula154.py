
import boto3
import io
from io import BytesIO


s3 = boto3.resource(
  service_name = 's3',
  region_name ='sa-east-1',
  aws_access_key_id = 'AKIAYA3EVBTEUBHTFB7K', 
  aws_secret_access_key = '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'

)
bucket = 'sivaldoaulapython'
prefix = 'imagens/'


for object_s3 in s3.Bucket(bucket).objects.filter(Prefix = prefix):
  if object_s3.key.endswith('png') or object_s3.key.endswith('PNG'):
    #print(object_s3)
    filename = object_s3.key.split('/')[1]
    print(filename)

#baixar as imagens
    body = object_s3.get()['Body'].read()
    imagem = io.BytesIO(body)
    with open(filename, 'wb') as f:
      f.write(imagem.getbuffer())