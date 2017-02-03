"""
.. module: lemur.plugins.lemur_aws.s3
    :platform: Unix
    :synopsis: Contains helper functions for interactive with AWS S3 Apis.
    :copyright: (c) 2015 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
import boto3
from cStringIO import StringIO


def write_to_s3(account_number, bucket_name, key, data, encrypt=True):
    """
    Use STS to write to an S3 bucket

    :param account_number:
    :param bucket_name:
    :param data:
    """
    client = boto3.resource('s3')

    b = client.Bucket(bucket_name)  # validate=False removes need for ListObjects permission

    b.upload_fileobj(StringIO(data), key, ExtraArgs={'ServerSideEncryption':'AES256'})
