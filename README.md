---


---

<h2 id="dynamic-hosts">Dynamic Hosts</h2>
<pre><code>ansible all -m ping -i ec2.py --list-hosts
ansible -i ec2.py -u ec2-user us-east-1b -m ping --list-hosts
ansible -b -i ec2.py -u ec2-user us-east-1b -m yum -a "name='*' state=latest" --private-key=keypairs/ec2_priv_key.pem
</code></pre>
<p><a href="https://aws.amazon.com/blogs/apn/getting-started-with-ansible-and-dynamic-amazon-ec2-inventory-management/">https://aws.amazon.com/blogs/apn/getting-started-with-ansible-and-dynamic-amazon-ec2-inventory-management/</a></p>
<h2 id="python">Python</h2>
<p>List all modules from Python console</p>
<pre><code>python
help("modules")
</code></pre>
<h2 id="boto">Boto</h2>
<p>cat ~/.boto</p>
<pre><code>[Credentials]
aws_access_key_id="XXXXXXXXXXXXXXXXXX"
aws_secret_access_key="xxxxxxxxxxxxxxxxxx"
</code></pre>
<h2 id="credentials">Credentials</h2>
<p><a href="https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/configuration.html">https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/configuration.html</a><br>
The mechanism in which boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials.<br>
The order in which Boto3 searches for credentials is:</p>
<ol>
<li>Passing credentials as parameters in the boto.client() method</li>
<li>Passing credentials as parameters when creating a Session object</li>
<li>Environment variables</li>
<li>Shared credential file (~/.aws/credentials)</li>
<li>AWS config file (~/.aws/config)<br>
6 .Assume Role provider</li>
<li>Boto2 config file (/etc/boto.cfg and ~/.boto)</li>
<li>Instance metadata service on an Amazon EC2 instance that has an IAM role configured.</li>
</ol>
<h2 id="how-to-specify-credentials-when-connecting-to-boto3-s3">How to specify credentials when connecting to boto3 S3?</h2>
<p>You can create a session:</p>
<pre><code>import boto3
session = boto3.Session(
    aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
    aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
)
</code></pre>
<p>Then use that session to get an S3 resource:</p>
<p><code>s3 = session.resource('s3')</code></p>
<p>You can get a client with new session directly like below.</p>
<pre><code>s3_client = boto3.client('s3',
                     aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
                     aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY,
                     region_name=REGION_NAME
                     )
</code></pre>
<h2 id="print-formatting">Print Formatting</h2>
<pre><code># Python program showing  
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and refering  
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))
</code></pre>
<hr>
<pre><code># print integer and float value
print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))  

# print integer value
print("Total students : % 3d, Boys : % 2d" %(240, 120))

# print octal value
print("% 7.3o"% (25))

# print exponential value
print("% 10.3E"% (356.08977))
</code></pre>
<hr>
<h3 id="iam">IAM</h3>
<ol>
<li>List IAM Users</li>
<li>List EC2 Instances</li>
<li>List RDS Instances</li>
<li>List S3 Buckets</li>
<li>List ECR Repos</li>
<li>List ECS Clusters</li>
</ol>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -h
usage: manage_aws-v1.1.py [-h] -s {iam,ec2,rds,s3,ecr,ecs} -i INPUT

optional arguments:
  -h, --help            show this help message and exit
  -s {iam,ec2,rds,s3,ecr,ecs}, --service {iam,ec2,rds,s3,ecr,ecs}
                        List instances of AWS services
  -i INPUT, --input INPUT
                        Path to AWS Credentials file in INI format
</code></pre>
<h2 id="iam-1">IAM</h2>
<pre class=" language-root"><code class="prism @PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating language-root">Username        Member Of Groups
--------------------------------
mcplus
linuxuser       network_admins, linux_admins, IT-OPS, IT-Dev
cloud_user
networkuser     linux_admins
mpython network_admins, linux_admins, marketing
jcleese
root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS#
</code></pre>
<h2 id="ec2">EC2</h2>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -s ec2 -i "/mnt/d/DevOpsProjects/Automating AWS/awscredentials.ini"
Instance ID             State            Private IP             Public IP
i-060709eeb61833873     pending         172.31.84.133           3.84.6.86
i-00c635b2fd0af14a2     running         10.10.10.147            3.227.11.23
i-09747831e5689ddeb     running         10.10.10.82             3.80.213.236
root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS#
</code></pre>
<h2 id="rds">RDS</h2>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -s rds -i "/mnt/d/DevOpsProjects/Automating AWS/awscredentials.ini"
Database Name   Database Endpoint                                                       Status
dbserver-001    dbadmin@dbserver-001.cnayjve5rxva.us-east-1.rds.amazonaws.com:3306      available
dbserver-002    dbadmin@dbserver-002.cnayjve5rxva.us-east-1.rds.amazonaws.com:3306      available
root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS#
</code></pre>
<h2 id="s3">S3</h2>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -s s3 -i "/mnt/d/DevOpsProjects/Automating AWS/awscredentials.ini"
Bucket Name
-----------------
data-471449
data-803398
</code></pre>
<h2 id="ecr">ECR</h2>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -s ecr -i "/mnt/d/DevOpsProjects/Automating AWS/awscredentials.ini"
Repository Name
-----------------
super/cool
deal/unbreaker
</code></pre>
<h2 id="ecs">ECS</h2>
<pre><code>root@PJPC-BBRPGE8:/mnt/d/DevOpsProjects/Automating AWS# ./manage_aws-v1.1.py -s ecs -i "/mnt/d/DevOpsProjects/Automating AWS/awscredentials.ini"
Cluster ARN
-----------------
arn:aws:ecs:us-east-1:722840993652:cluster/example-cluster
arn:aws:ecs:us-east-1:722840993652:cluster/another-cluster
</code></pre>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUwODI1ODQzOV19
-->