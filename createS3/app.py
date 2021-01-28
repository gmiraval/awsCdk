#!/usr/bin/env python3

from aws_cdk import core

from create_s3.create_s3_stack import CreateS3Stack


app = core.App()
CreateS3Stack(app, "create-s3")

app.synth()
