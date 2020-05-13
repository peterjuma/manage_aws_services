# CLI Application To Manage AWS Services

This is a simple command line interface (CLI) application that allows users to take an inventory of resources that are currently provisioned.
Working with Boto3 and Python libraries, we use Python scripts to interact with infrastructure provided by Amazon Web Services (AWS).

You can list resources of the following AWS services:
1. IAM users
2. EC2 instances
3. RDS instances
4. S3 buckets
5. ECR repos
6. ECS clusters


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

**Python and Pip**
We will be using Python 3.x for this project.

First, check to see if Python is already installed. You can do this by typing which python in your shell. If Python is installed, the response will be the path to the Python executable.
If Python is not installed, go to the [Python.org](https://www.python.org/downloads/) website for information on downloading and installing Python for your particular operating system.

Check your version of Python by typing `python -V`.

The next thing we’ll need is pip, the Python package manager. We’ll use pip to install the Boto3 library. You can check for pip by typing `which pip`. If pip is installed, the response will be the path to the pip executable.
If pip is not installed, follow the [instructions at pip.pypa.io](https://pip.pypa.io/en/stable/installing/) to get pip installed on your system.

Check your version of pip by typing `pip -V`. Your version of pip should be 9.0.1 or newer.

With Python and pip installed, we can install the packages needed for our application.

**AWS Credentials**

Store your AWS account access credentials in a file in INI format below. Take note of the file path.

```
[credentials]
AWS_ACCESS_KEY_ID = XXXXXXXXXXX
AWS_SECRET_ACCESS_KEY = XXXXXXXXXXX
AWS_REGION = XXXXXXXXXXX
```

The file will be passed to the application as a command line argument. See **Application Usage** section.


### Installing


Using the pip command, install Boto3:

```
pip install awscli boto3 -U --ignore-installed six
```

Other required libraries are `ConfigParser` and `argparse`:
```
pip install ConfigParser
pip install argparse
```

We now have our environmane ready to run our application.

## Application Usage
Now that we have our installation ready, lets go through how to put the application to use in your environment

**Comandline Options**


`manage_aws_services.py -s [--service] {AWS service name} -i [--input] {AWS credentials file path}`


```
./manage_aws_services.py -h
usage: manage_aws_services.py [-h] -s {iam,ec2,rds,s3,ecr,ecs} -i INPUT

optional arguments:
  -h, --help            show this help message and exit
  -s {iam,ec2,rds,s3,ecr,ecs}, --service {iam,ec2,rds,s3,ecr,ecs}
                        List instances of AWS services
  -i INPUT, --input INPUT
                        Path to AWS Credentials file in INI
```

**Note**: The allowed services are `iam`, `ec2`, `rds`, `s3`, `ecr` and `ecs`.



**List AWS IAM Users**

Command:

`./manage_aws_services.py -s iam -i "/path/to/awscredentials.ini"`

Output:
```
Username        Member Of Groups
--------------------------------
mcplus
linuxuser       network_admins, linux_admins, IT-OPS, IT-Dev
cloud_user
networkuser     linux_admins
mpython         network_admins, linux_admins, marketing
jcleese
```


**List AWS EC2 Instances**

Command:

`./manage_aws_services.py -s ec2 -i "/path/to/awscredentials.ini"`

Output:
```
Instance ID             State            Private IP             Public IP
i-060709eeb61833873     pending         172.31.84.133           3.84.6.86
i-00c635b2fd0af14a2     running         10.10.10.147            3.227.11.23
i-09747831e5689ddeb     running         10.10.10.82             3.80.213.236
```

**List AWS RDS Instances**

Command:

`./manage_aws_services.py -s rds -i "/path/to/awscredentials.ini"`

Output:
```
Database Name   Database Endpoint                                                       Status
dbserver-001    dbadmin@dbserver-001.cnayjve5rxva.us-east-1.rds.amazonaws.com:3306      available
dbserver-002    dbadmin@dbserver-002.cnayjve5rxva.us-east-1.rds.amazonaws.com:3306      available

```


**List AWS S3 Buckets**

Command:

`./manage_aws_services.py -s s3 -i "/path/to/awscredentials.ini"`

Output:
```
Bucket Name
-----------------
data-471449
data-803398
```


**List AWS ECR Repositories**

Command:

`./manage_aws_services.py -s ecr -i "/path/to/awscredentials.ini"`

Output:

```
Repository Name
-----------------
super/cool
deal/unbreaker
```


**List AWS ECS clusters**

Command:

`./manage_aws_services.py -s ecs -i "/path/to/awscredentials.ini"`

Output:

```
Cluster ARN
-----------------
arn:aws:ecs:us-east-1:722840993652:cluster/example-cluster
arn:aws:ecs:us-east-1:722840993652:cluster/another-cluster
```


## Authors

* **Peter Juma** - *Initial work* - [peterjuma](https://gitlab.com/peterjuma)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
