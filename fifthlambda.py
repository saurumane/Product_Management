import json
import boto3
import csv


def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket = 'pmsprojecttesting'
    input_key = 'input/saurabh.csv'
    output_key = 'output/saurabh_processed40_to_50.csv'

    input_file_path = '/tmp/saurabh.csv'
    output_file_path = '/tmp/saurabh_processed40_to_50.csv'

    # Download the input file from S3
    s3_client.download_file(bucket, input_key, input_file_path)

    # Process and write rows 40 to 50 to a new file
    new_rows = []
    with open(input_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader, start=1):
            if 42 <= index <= 51:
                new_rows.append(row)

    # Write the selected rows to a new file
    with open(output_file_path, 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerows(new_rows)

    # Upload the processed file to the output folder in S3
    s3_client.upload_file(output_file_path, bucket, output_key)

    response = {
        "statusCode": 200,
        "body": "\"Processed rows 40 to 50 and saved to output folder\"",
        "success": True
    }
    return response