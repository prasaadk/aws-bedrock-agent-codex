import json

def lambda_handler(event, context):
    """Sample Lambda handler for Bedrock Agent operations."""
    print("Received event:", json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Bedrock agent"})
    }
