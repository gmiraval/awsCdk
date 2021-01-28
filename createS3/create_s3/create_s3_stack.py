from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as iam,
    core
)

class CreateS3Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # create s3 bucket
        s3 = _s3.Bucket(self, "mirgorS3",bucket_name="mirgor")

        #add tags bucket
        core.Tags.of(s3).add("CostCenter", "CTO")
        core.Tags.of(s3).add("Project", "SmartHome")
        core.Tags.of(s3).add("Vendor", "Mirgor")

        #create user & group
        group = iam.Group(self, "mirgorGroup", group_name="mirgor")
        #user = iam.User(self, "mirgorUser",user_name="mirgor",password=core.SecretValue.plain_text("1234"))
        user = iam.User(self, "mirgorUser",user_name="mirgor")

        #adduser to group
        group.add_user(user)

        # add policy to group
        policy = iam.Policy(
            self, "MyPolicy",
            policy_name='mirgorS3'
        )

        policy_statement = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["s3:*",],
            resources=[f"{s3.bucket_arn}*"],
        )
        
        policy.add_statements(policy_statement)

        #attach policy to group
        policy.attach_to_group(group)
        group.attach_inline_policy(policy)
       
        ##get access keys
        key = iam.CfnAccessKey(self,"mirgorAccessKey",user_name=user.user_name)

        core.CfnOutput(self, 'AccessKeyId', value=key.ref)
        core.CfnOutput(self, 'secretAccessKey', value=key.attr_secret_access_key)