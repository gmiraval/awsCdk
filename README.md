# awsCdk
Cdk scripts for aws

## python cdk
https://cdkworkshop.com/30-python.html
https://docs.aws.amazon.com/cdk/api/latest/python/index.html

https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html

### examples
https://github.com/aws-samples/aws-cdk-examples/tree/master/python

## initial config
requires node, pip , python3 , virtualenv & python3-venv
npm install -g aws-cdk

## init project
mkdir my-project
cd my-project
cdk init app --language python

source .venv/bin/activate

note: You may recognize this as the Mac/Linux command to activate a virtual environment.

### inisde virtual env  activate dependencies 
python -m pip install -r requirements.txt

### install required libs
The AWS CDK core module is named aws-cdk.core. AWS Construct Library modules are named like aws-cdk.SERVICE-NAME. The service name includes an aws prefix. If you're unsure of a module's name, search for it at PyPI. For example, the command below installs the modules for Amazon S3 and AWS Lambda.

python -m pip install aws-cdk.aws-s3 aws-cdk.aws-lambda

#### required libs
python -m pip install aws-cdk.aws-s3


### first time usage of cdk @ a given account/region -> cdk bootstrap
(.venv) gmiraval@gmiraval:~/wk/awsCdk/createS3$ cdk --profile CTO bootstrap
 ⏳  Bootstrapping environment aws://044237255272/us-west-2...
CDKToolkit: creating CloudFormation changeset...
[██████████████████████████████████████████████████████████] (3/3)

### deploy
cdk --profile CTO synth
cdk --profile CTO diff
cdk --profile CTO deploy


 ✅  Environment aws://044237255272/us-west-2 bootstrapped.
(.venv) gmiraval@gmiraval:~/wk/awsCdk/createS3$ 

### remove deployed stack -> destroy
(.venv) gmiraval@gmiraval:~/wk/awsCdk/createS3$ cdk --profile CTO destroy
Are you sure you want to delete: create-s3 (y/n)? y
create-s3: destroying...
11:19:12 AM | DELETE_IN_PROGRESS   | AWS::CloudFormation::Stack | create-s3

 ✅  create-s3: destroyed

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

 ### to use a given profile use --profile
 
 cdk --profile CTO diff

 cdk gets credentials & region from profiles (if its configured)

 #### check profile region
 aws configure get region --profile CTO


