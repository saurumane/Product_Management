import json
import boto3

def lambda_handler(event, context):
    #execute step function
    client=boto3.client('stepfunctions')
    response=client.start_execution(stateMachineArn='arn:aws:states:ap-south-1:665842648785:stateMachine:MyStateMachine-4z834p9xf')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from stepfunction!')
    }

""" to all who are on this code, please add trigger of input folder of bucket to this lambda and
paste your arn of state machine then only run this code, otherwise your code will not run."""