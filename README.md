# Ada AWS Examples

Some small examples to illustrate how to interact with AWS with code.

# Requirements

- python3

# Getting Started

Make sure to install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [set up your credentials beforehand.](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

```sh
> aws configure
```
Set up the virtual environment:

```sh
> python3 -m virtalenv venv
> source ./venv/bin/activate
> (venv) make install
```

```sh
> python main.py -h
usage: AdaAwsExamples [-h] [-l] [-c CREATE] [-d DELETE]

A few s3 examples

options:
  -h, --help            show this help message and exit
  -l, --list
  -c CREATE, --create CREATE
                        create a bucket. ex: --create my-bucket-name
  -d DELETE, --delete DELETE
                        delete a bucket. ex: --delete my-bucket-name
```

# List buckets

```sh
> python main.py -l
Bucket name: cat-pictures-logyball
Bucket name: logyball-terraform
```
