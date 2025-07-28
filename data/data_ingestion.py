import io
import os
from minio import Minio
import glob
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
minio_url = os.getenv("MINIO_EXTERNAL_URL")
minio_bucket_name = os.getenv("MINIO_BUCKET_NAME")

def upload_to_minio(minio_client, bucket_name, data, object_name):
    csv_buffer = io.StringIO()
    data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=io.BytesIO(csv_buffer.getvalue().encode('utf-8')),
        length=len(csv_buffer.getvalue().encode('utf-8')),
        content_type='text/csv'
    )
    
    
    
def main():
    minio_client = Minio(minio_url, access_key=minio_access_key, 
                        secret_key=minio_secret_key, secure=False)
    csv_files = glob.glob("data/*.csv")
    for csv_file in csv_files:
        data = pd.read_csv(csv_file)
        upload_to_minio(minio_client, minio_bucket_name, data, os.path.basename(csv_file))
        
        
if __name__ == '__main__':
    main()