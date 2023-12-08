import boto3, sys, argparse
from pprint import pprint


def list_buckets(s3):
    all_buckets = s3.list_buckets()
    buckets = all_buckets.get('Buckets', [])
    for b in buckets:
       print(f"Bucket name: { b.get('Name', 'name not found') }")

def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    list_buckets(s3)

def delete_bucket(s3, bucket_name):
    s3.delete_bucket(Bucket=bucket_name)
    list_buckets(s3)


def main():
    parser = argparse.ArgumentParser(
        prog='AdaAwsExamples',
        description='A few s3 examples')
    parser.add_argument('-l', '--list', action='store_true')
    parser.add_argument('-c', '--create')
    parser.add_argument('-d', '--delete')
    args = parser.parse_args()

    s3_client = boto3.client('s3')

    if args.list:
        list_buckets(s3_client)
    if args.create:
        create_bucket(s3_client, args.create)
    if args.delete:
        delete_bucket(s3_client, args.delete)
    

if __name__ == '__main__':
    main()
