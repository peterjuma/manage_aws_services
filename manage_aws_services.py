#!/usr/bin/env python3
from configparser import ConfigParser
import boto3
import argparse

# Read & parse commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--service', dest='aws_service', choices=['iam', 'ec2', 'rds', 's3', 'ecr', 'ecs'], help="List instances of AWS services", required=True)
parser.add_argument('-i', '--input', type=str, help="Path to AWS Credentials file in INI format", required=True)
args = parser.parse_args()
svc = args.aws_service
credentials_file = args.input

# Read & parse AWS credentials file
def config(filename, section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to credentials
    aws = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            aws[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return aws

# Get credentials parameters (params['aws_access_key_id'], params['aws_secret_access_key'], params['aws_region'])
params = config(credentials_file,'credentials')

# Create a session
session = boto3.Session(
    aws_access_key_id=params['aws_access_key_id'],
    aws_secret_access_key=params['aws_secret_access_key'],
    region_name=params['aws_region'],
)

# Get list of users and groups
def iam_list():
    iam = session.client('iam')
    user = {}
    for userlist in iam.list_users()['Users']:
        userGroups = iam.list_groups_for_user(UserName=userlist['UserName'])
        user[userlist['UserName']]={'groups':''}
        groupnames = [groupName['GroupName'] for groupName in userGroups['Groups']]
        user[userlist['UserName']] = groupnames
    return user

# List ec2 instances
def ec2_list_instances():
    ec2 = session.resource('ec2')
    instances = ec2.instances.all()
    return instances


# List RDS instances
def rds_list_instances():
    rds = session.client('rds')
    dbs = rds.describe_db_instances()
    return dbs

# List S3 buckets
def s3_list_buckets():
    s3 = session.resource('s3')
    s3buckets=s3.buckets.all()
    return s3buckets

# List ECR repos
def ecr_list_repos():
    ecr = session.client('ecr')
    repos = ecr.describe_repositories()['repositories']
    return repos

# List ECS clusters
def ecs_list_clusters():
    ecs = session.client('ecs')
    clusters = ecs.list_clusters()['clusterArns']
    return clusters


def menu():
     if svc == 'iam':
         users = iam_list()
         print("Username\tMember Of Groups")
         print("--------------------------------")
         for user in users:
             print("{}\t{}".format(user, ', '.join(users[user])))
     elif svc == 'ec2':
         instances = ec2_list_instances()
         print("Instance ID\t\tState\t\t Private IP\t\tPublic IP")
         for instance in instances:
             print("{}\t{}\t\t{}\t\t{}".format(instance.id, instance.state['Name'], instance.private_ip_address,
                                        instance.public_ip_address))
     elif svc == 'rds':
         dbs = rds_list_instances()
         try:
             print("Database Name\tDatabase Endpoint\t\t\t\t\t\t\tStatus")
             for db in dbs['DBInstances']:
                 print("{}\t{}@{}:{}\t{}".format(db['DBInstanceIdentifier'],db['MasterUsername'],db['Endpoint']['Address'],db['Endpoint']['Port'],db['DBInstanceStatus']))
         except Exception as error:
             print(error)
     elif svc == 's3':
         s3 = s3_list_buckets()
         print("Bucket Name")
         print("-----------------")
         for bucket in s3:
             print(bucket.name)

     elif svc == 'ecr':
         repos = ecr_list_repos()
         print("Repository Name")
         print("-----------------")
         for repo in repos:
             print(repo['repositoryName'])
     elif svc == 'ecs':
         clusters=ecs_list_clusters()
         print("Cluster ARN")
         print("-----------------")
         for cluster in clusters:
             print(cluster)

if __name__ == "__main__":
    menu()
