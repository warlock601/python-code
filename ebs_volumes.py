# This prog is to get all the avaiable volumes in a spoecific aws region in your account using boto3 module
# we needed access and secret access key as we're trying from the local IDE, if we're doing it inside Lambda function in aws, then we don't need keys
# In boto3.client(), we'll need to mention keys and region as well

import boto3

aws_access_key =  'your aws access key'
aws_secret_key = 'your aws secret access key'
aws_region = 'region in which you wanna find volumes'

ec2_client = boto3.client('ec2',aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_key,region_name=aws_region)

response=ec2_client.describe_volumes()

for volume in response['Volumes']:
    volume_id = volume['VolumeId']
        #volume_all.append(volume_id)   

    print(volume_id)
