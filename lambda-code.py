import json
import boto3

# Creando una instancia de la tabla DynamoD y s3
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Nombre de la tabla en DynamoDB
table = dynamodb.Table('mitabla2')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    # Obtiene el nombre del bucket y la clave del archivo JSON del evento de S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(key)
    
    # Descarga el archivo JSON desde S3
    response = s3.get_object(Bucket=bucket, Key=key)
    json_data = response['Body'].read().decode('utf-8')

    # Parsea el JSON
    data = json.loads(json_data)

    # Inserta los datos en DynamoDB utilizando el recurso
    response = table.put_item(
        Item={
            'ID': data['ID'],
            'Nombre': data['Nombre'],
            'Correo electrónico': data['Correo electrónico'],
            'Fecha de registro': data['Fecha de registro']
        }
        
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Datos guardados en DynamoDB exitosamente.')
    }
