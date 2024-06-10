import sys
import json

def handler(event, context):
    # Construir la respuesta
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "Hello from Lambda!"})
    }

    return response
