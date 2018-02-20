"""
READ ME:

The following is just a list of commands to use in python and in a linux terminal for getting
aws-client-v1.py to run on an AWS EC2 client.

For this particular example, it is assumed that rest-api-service-basic-v1.py has been launched in order
to create a mock-up rest-api service.
"""

# in cmd:
    # aws configure --> supply the aws key pairs
    # aws ec2 describe-instances
    # aws opsworks --region us-west-2 describe-user-profiles
    # https://aws.amazon.com/cli/

# in python3.5
# see http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#instance

import sys
import boto3

#-----------#
# view ec2 instance
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
# monitor ec2 instances and attributes of those instances
instance = ec2.Instance('<<instance id>>')

#-----------#
# identify aws-client script
jp_script = r'\c\...\aws-client-v1.py'

#-----------#
# in terminal: chmod 400 /path/my-key-pair.pem  # provide the key credential file needed for ssh-ing into the instance
# in terminal: ssh -i /path/my-key-pair.pem(.cer) USER@Public DNS

# We are now in the AWS EC2 instance's terminal

"""
In order to run the scripts on ec2, store aws-client-v1.py on Github as a repo 
or as a gist and clone it into the aws ec2.

Run store aws-client-v1.py after ssh-ing directly into the host.
"""