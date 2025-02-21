import os

import boto3
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION", "us-west-1"),
    endpoint_url=os.getenv("DYNAMODB_URL", "http://dynamodb:8000"),
)


def create_tables():
    """kreira tablice ako ne postoje"""
    try:
        invoices_table = dynamodb.create_table(
            TableName="Invoices",
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        invoices_table.wait_until_exists()
        print("TAblica 'invoices' uspješno kreirana.")
    except Exception as e:
        print(f"Tablica već postoji: {e}")

    try:
        users_table = dynamodb.create_table(
            TableName="users",
            KeySchema=[{"AttributeName": "username", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "username", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        users_table.wait_until_exists()
        print("Tablica 'users' uspješno kreirana.")
    except Exception as e:
        print(f"Tablica 'users' već postoji: {e}")


# Pokretanje funkcije pri incijalitaciji
if __name__ == "__main__":
    create_tables()
