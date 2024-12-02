import json

def lambda_hamdler(event, context):
    return {
     'StatusCode': 200,
     'body': json.dumps('Hello from CICD github actions worklow vs code')     
       
    } 
