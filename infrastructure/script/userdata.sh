#!/bin/bash
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
export AWS_DEFAULT_REGION=us-west-2
cd /home/ec2-user
aws s3 cp s3://patent-data-informer/patent-data-server.zip patent-data-server.zip
unzip patent-data-server.zip
rm patent-data-server.zip
pip3 install -r requirements.txt
cd source
python3 main.py
