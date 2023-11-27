import boto3
from botocore.exceptions import ClientError


def send_email():
    sender_email = 'saurumane7032@gmail.com'
    recipient = 'sauru00002@gmail.com'
    aws_region = 'ap-south-1'

    ses_client = boto3.client('ses', region_name=aws_region)

    subject = 'Processing File chunks'
    body_text = "Hello From AWS Step function services, this message is to inform you that, I have successfully executed step function and processed the file"
    CHARSET = "UTF-8"

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=sender_email
        )
    except ClientError as e:
        return str(e)
    else:
        return "Email Sent Successfully"


def lambda_handler(event, context):
    result = send_email()
    return {
        'status_code': 200,
        'body': result
    }
"""
before using this code you need to make sure to enable simple email service and you should be able to verify
your email address first and once you verify you can only send mail to verified address only because 
of sandbox limitations of aws service for testing purpose send your mail with your name in it to 
saurumane7032@gmail.com 
thank you """