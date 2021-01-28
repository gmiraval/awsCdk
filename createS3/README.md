#s3 creation example
script used to generate an s3 bucket, user, credentials & policy to access only this bucket.

#usage
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=yyy
export AWS_DEFAULT_REGION=us-west-2

gmiraval@gmiraval:~$ aws s3 ls s3://mirgor
gmiraval@gmiraval:~$ aws s3 cp test.txt s3://mirgor/test1/test.txt
upload: ./test.txt to s3://mirgor/test1/test.txt              
gmiraval@gmiraval:~$ aws s3 ls s3://mirgor
                           PRE test1/




