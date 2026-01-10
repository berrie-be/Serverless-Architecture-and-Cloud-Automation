import boto3
from datetime import datetime, timedelta, timezone

ec2_client = boto3.client('ec2')

deleted_snapshot = []
snapshot_not_older_than_30days = []

cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)

response = ec2_client.create_snapshot(VolumeId='vol-0025978106686fc36')

responsee = ec2_client.describe_snapshots(Filters=[
        {
            'Name': 'volume-id',
            'Values': ['vol-0025978106686fc36']
        }])

for i in responsee['Snapshots']:
    if i['StartTime'] < cutoff_date:
        snapshot = i['SnapshotId']
        res = ec2_client.delete_snapshot(SnapshotId=snapshot)
        deleted_snapshot.append(i['SnapshotId'])
    else:
        snapshot_not_older_than_30days.append(i['SnapshotId'])

print("Deleted Snapshots are:",deleted_snapshot)   
print("Snapshot not older than 30 days:", snapshot_not_older_than_30days)
