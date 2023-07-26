import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd 
import parquet

s3 = boto3.client('s3', aws_access_key_id='key id', aws_secret_access_key='key', region_name='us-east-1')
bucket_name = 'parquet-bsc'


bsc_local_path = 'Your Path/sample.parquet'
bsc_key='dex_trades_tx/2020-09-12_410000_C56AEF483BA69257_5000.parquet'

filename='2020-09-12_410000_C56AEF483BA69257_5000.parquet'

file_obj = s3.download_file(bucket_name, bsc_key, bsc_local_path)

df = pd.read_parquet(bsc_local_path)

print(df.head()) 