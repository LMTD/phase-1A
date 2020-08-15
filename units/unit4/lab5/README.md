# LMTD Phase One - Unit 4 - Lab 5
Working with Amazon Web Services and Python

## About This Lab
This lab is designed to extend your knowledge of Python, by giving you an opportunity to write a cloud-based application using the `boto3` Amazon SDK. Amazon Web Services provide developers a number of tools to add scalable computing, storage, and processing power to your workflow.
 
## About [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
The `boto3` SDK is the Python SDK for AWS. It allows you to directly connect to AWS resources from your Python scripts. 

### Installing and Configuring Boto3

In order to get the boto3 library into your Python code you need to install the `boto3` module in your Python code:

```
pip install boto3
```

To make it run with your AWS account, you'll need to add valid credentials that you receive from AWS IAM. If you don't have a user with permissions to use S3 you can [create a new user on your AWS account]().

The IAM account will present you with user credentials that you will need to configure your account with boto3.

With your new credentials, you need to create a new file at the path: `~/.aws/credentials`

```
touch ~/.aws/credentials

```

Open the file and paste the information below with your credentials:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
After you save this file, you will have a default profile that boto3 can use to connect to your AWS instance.

The last step you have to do to set-up your account is add a configuration file that tells boto3 the [AWS region](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) you want to interact with.

Create a new file like so:
```
touch ~/.aws/config
```

Add the following lines into the file:
```
[default]
region = YOUR_PREFERRED_REGION

```

Save your file and you're ready to roll!

### boto3 Client vs Resource

boto3 essentially calls AWS APIs through your Python code. There are two distinct methods of accessing the AWS APIs:

**Client:** Access to low-level services and functions
**Resource:** Access to higher level object-oriented services and functions

You can use either to interact with a service like S3. The easiest way to connect would be to pass in the name of the service you want to connect to and create a boto3 instance variable you can refere to later. 
```
import boto3

# to connect to the s3 client 
s3_client = boto3.client('s3')

# to connect to the s3 resource
s3_resource = boto3.resource('s3')

# remember you can use either but always check the documentation!
```
When you use the *client library*, most functions will return a Python Dictionary response. In order to get the information you need then, you'll have to parse the dictionary yourself. If you use the *resource library*  the boto3 SDK will do some of that work for you.

Boto3 generates the client and the resource from different definitions. As a result, you may find cases in which an operation supported by the client isn’t offered by the resource. Here’s the interesting part: you don’t need to change your code to use the client everywhere. For that operation, you can access the client directly via the resource like so: `boto3.resource('s3').meta.client`.

### Common Operations

#### Creating a Bucket
To start off, you need an S3 bucket. To create one programmatically, you must first choose a name for your bucket. Remember that this name must be unique throughout the whole AWS platform, as bucket names are DNS compliant. If you try to create a bucket, but another user has already claimed your desired bucket name, your code will fail. Instead of success, you will see the following error: botocore.errorfactory.BucketAlreadyExists.

You can increase your chance of success when creating your bucket by picking a random name. You can generate your own function that does that for you. In this implementation, you’ll see how using the uuid module will help you achieve that. A UUID4’s string representation is 36 characters long (including hyphens), and you can add a prefix to specify what each bucket is for.

```
import uuid
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

```

#### Uploading a File

There are a couple ways to upload a file: From an Object instance, From a Bucket instance, From the client. In all cases you need to provide the Filename and the bucket you want to save them at.

```
import boto3

# to connect to the s3 client 
s3_client = boto3.client('s3')

# to connect to the s3 resource
s3_resource = boto3.resource('s3')

# Uploading using the client
s3_client.upload_file(
    Filename=first_file_name, Bucket=first_bucket_name,
    Key=first_file_name)

# Uploading using an Object Instance
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name)

# Uploading using a Bucket Instance
s3_resource.Bucket(first_bucket_name).upload_file(
    Filename=first_file_name, Key=first_file_name)

```

#### Downloading a File
To download a file from S3 locally, you’ll follow similar steps as you did when uploading. But in this case, the Filename parameter will map to your desired local path. This time, it will download the file to the tmp directory:

```
import boto3

# to connect to the s3 client 
s3_client = boto3.client('s3')

# to connect to the s3 resource
s3_resource = boto3.resource('s3')

s3_client.download_file('bucket_name', 'file_name', 'returned_file_name')


s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/tmp/{first_file_name}') # Python 3.6+
```

#### Deleting an Object
```
s3_resource.Object(second_bucket_name, first_file_name).delete()
```

## Lab 5 Objective
Working individually you will create a Python program that saves some data to AWS S3.

Your goal is to create a Python program that will generate an HTML file and save it to our class bucket in S3.

### Requirements

* Your program must be connected to git and you will submit your link to Github at the end of class. We will look for you to be making several commits to save your work.

* Your program must create a class called `HtmlDocument` that lets you initialize some HTML for a new document.

* Your program must create a class called `HtmlManager` that defines functions that let you create a new HTML document, and save the document to your files. 

* Your program must create a class called `AWSManager` that defines the connections to `boto3` and some functions that let you save your file to `S3`.

## Collaborating with the class
Feel free to ask questions to the folks in your breakout groups but everyone will have to submit the Lab on their own.

## Submission
Your program should save a file called `yourname.html` to our class bucket in S3. 

Please share a copy of your Github link via the Lab submission form shared in Slack when you've finished. 

## Resources
* [Uploading files with boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
* [Boto3, S3, AWS](https://realpython.com/python-boto3-aws-s3/)
* [Writing HTML with Python](https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python)
* [Create an HTML string with tags](https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-15.php)