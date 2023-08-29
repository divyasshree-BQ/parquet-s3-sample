import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd 
import parquet

s3 = boto3.client('s3', aws_access_key_id='your id', aws_secret_access_key='your key', region_name='us-east-1')
bucket_name = 'parquet-bsc'


bsc_local_path = 'C:/Users/divyn/Downloads/sample.parquet'
bsc_key='dex_trades_tx/2020-09-12_410000_88573E9FA803AF8D_10000.parquet'

filename='2020-09-12_410000_88573E9FA803AF8D_10000.parquet'

file_obj = s3.download_file(bucket_name, bsc_key, bsc_local_path)

df = pd.read_parquet(bsc_local_path)

df.to_csv('parquet_output.csv', index=False)