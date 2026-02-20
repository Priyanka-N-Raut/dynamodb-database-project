import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('interns')

response = table.scan()

print("Stored Items:\n")

for item in response['Items']:
    print(item)
