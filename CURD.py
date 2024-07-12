import json
import boto3
from decimal import Decimal

dynamo = boto3.resource('dynamodb').Table('http-crud-tutorial-items')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    status_code = 200
    headers = {
        'Content-Type': 'application/json'
    }
    body = ""

    try:
        route_key = event['routeKey']
        if route_key == "DELETE /items/{id}":
            dynamo.delete_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = f"Deleted item {event['pathParameters']['id']}"
        elif route_key == "GET /items/{id}":
            response = dynamo.get_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = response.get('Item', {})
        elif route_key == "GET /items":
            response = dynamo.scan()
            body = response.get('Items', [])
        elif route_key == "PUT /items":
            request_json = json.loads(event['body'])
            dynamo.put_item(
                Item={
                    'id': request_json['id'],
                    'price': request_json['price'],
                    'name': request_json['name']
                }
            )
            body = f"Put item {request_json['id']}"
        else:
            raise ValueError(f"Unsupported route: {route_key}")
    except Exception as e:
        status_code = 400
        body = str(e)
    finally:
        body = json.dumps(body, cls=DecimalEncoder)

    return {
        'statusCode': status_code,
        'body': body,
        'headers': headers
    }
