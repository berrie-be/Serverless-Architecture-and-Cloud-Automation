import boto3

s3_client = boto3.client('s3')

res = s3_client.list_buckets()
bucket_names = []
AES256_names = []
kms_names = []

for i in res['Buckets']:
    bucket_names.append(i['Name'])

for name in bucket_names:
    if "kaveri" in name:
        try:
            response = s3_client.get_bucket_encryption(Bucket=name)
            encryption = response['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            if encryption == "AES256":
                AES256_names.append(name)
            elif encryption == "aws:kms":
                kms_names.append(name)
        except:
            print("Error")

print("Buckets with Amazon S3 managed keys", AES256_names)
print("Buckets with Amazon S3 managed keys", kms_names)

