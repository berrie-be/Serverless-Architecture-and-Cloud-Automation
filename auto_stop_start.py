import boto3

ec2_client = boto3.client('ec2')

res = ec2_client.describe_tags()

start_instance_ids = []
stop_instance_ids = []

for i in res['Tags']:
    if i['ResourceType'] == "instance" and i['Key'] == "Action" and i['Value'] == "Auto-Start":
        response_start = ec2_client.start_instances(InstanceIds=[i['ResourceId']])
        start_instance_ids.append(i['ResourceId'])
    if i['ResourceType'] == "instance" and i['Key'] == "Action" and i['Value'] == "Auto-Stop":
        response_stop = ec2_client.stop_instances(InstanceIds=[i['ResourceId']])
        stop_instance_ids.append(i['ResourceId'])

print("Instances Started:", start_instance_ids)
print(stop_instance_ids)
