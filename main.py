import boto3, argparse


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
    parser.add_argument('-l', '--list', action='store_true', help="list all available buckets")
    parser.add_argument('-c', '--create', help="create a bucket. ex: --create my-bucket-name")
    parser.add_argument('-d', '--delete', help="delete a bucket. ex: --delete my-bucket-name")
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
