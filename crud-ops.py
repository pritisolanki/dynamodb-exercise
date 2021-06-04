# AWS Dynamodb : Learning Purpose
# crud-ops is a python script to setup CRUD operation on Movie table. Author plays with multiple ways to 
# fetch the data

from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

def get_all_movies_inYear(yearReleased, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    print(f"Get year, title, genres, and lead actor")

    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=Key('year').eq(yearReleased)
    )
    return response['Items']

if __name__ == '__main__':
    #get all movies for specific year
    year_movies = get_all_movies_inYear(2010)
    if year_movies:
        print(f"Movies released in 2010")
        for x in year_movies:
            print(f"{x['title']}")

    #Search specific movie
    movie = get_movie("Dance with Me", 1998)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)