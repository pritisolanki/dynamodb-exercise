'''
This python script is creating a dynamodb table 
'''
import boto3
import logging

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb= boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.create_table(
        TableName = 'Movies',
        KeySchema = [
            {
                'AttributeName' : 'year',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName' : 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'year',
                'AttributeType':'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType' : 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 10
        }
    )    
    return table

if __name__ == '__main__':
    #movie_table = create_movie_table()
    print("Table status: ",movie_table.table_status)