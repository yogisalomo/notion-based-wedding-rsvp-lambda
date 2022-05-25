import json
import requests
import os


def lambda_handler(event, context):
    url = "https://api.notion.com/v1/pages"

    payload = {
        "parent": {
            "database_id": os.environ['DATABASE_ID'],
        },
        "properties": {
            "name": {
                "title": [
                    {
                        "text": {
                            "content": event['name'],
                        },
                    },
                ],
            },
            "phone": {
                "phone_number":  event['phone']
            },
            "email": {
                "email": event['email']
            },
            "event": {
                "select": {
                    "name": event['event'],
                },
            },
            "num_person": {
                "number": event['num_person'],
            },
            "is_attending": {
                "checkbox": event['is_attending'],
            },
        }
    }
    
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ['NOTION_KEY']
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://www.yogi-and-lorenz-for.life',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response.text)
    }
