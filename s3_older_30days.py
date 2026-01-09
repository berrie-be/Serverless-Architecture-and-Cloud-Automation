import boto3
from datetime import datetime, timedelta, timezone

cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)

s3_client = boto3.client('s3')

res = s3_client.list_objects(Bucket='kaveri-automate-bucket')
object_names = []
deleted_objects = []

for i in res['Contents']:
    object_names.append(i['Key'])
    

for name in object_names:
    print(name)
    response = s3_client.head_object(Bucket='kaveri-automate-bucket', Key=name)
    metadata = response.get('Metadata', {})
    if metadata:
        if 'original-modified-date' in metadata:
            date_str = metadata['original-modified-date']
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            

            if date < cutoff_date:
                deletion = s3_client.delete_object(Bucket='kaveri-automate-bucket', Key=name)
                deleted_objects.append(name)

print("Deleted Objects:", deleted_objects)
