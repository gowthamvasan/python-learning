from operator import index
import boto3
import pandas as pd

def get_s3_buckets():
    s3 = boto3.client("s3")
    s3_list = pd.DataFrame()
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        bucket_name=bucket['Name']
        #print(bucket_name)
        response = s3.get_bucket_location(
                    Bucket=bucket_name,
                )
        location=response['LocationConstraint']
        s3_list = s3_list.append({
            'location': location,
            'bucket_name' : bucket_name
        }, ignore_index=True)
    s3_list.groupby(by='location')
    print(s3_list)
    s3_list.to_excel("output.xlsx",index=False) 

get_s3_buckets()