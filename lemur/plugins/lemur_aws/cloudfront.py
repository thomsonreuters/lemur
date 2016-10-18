"""
.. module: lemur.plugins.lemur_aws.aws
    :platform: Unix
    :copyright: (c) 2016 by Thomson Reuters
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: David Loutsch <david.loutsch@thomsonreuters.com>
"""
import time
from lemur.plugins.lemur_aws.sts import assume_service
from botocore.exceptions import ClientError


def attach_certificate_to_cloudfront(account_number, region, name, certificate_id):
    """
    Attaches a certificate to a listener, throws exception
    if certificate specified does not exist in a particular account.

    :param account_number:
    :param region:
    :param name:
    :param certificate_id:
    """
    cloudfront = assume_service(account_number, 'cloudfront', region)
    distro = cloudfront.get_distribution_config(Id=name)
    etag = distro.get('ETag')
    distro.get('DistributionConfig').get('ViewerCertificate')['IAMCertificateId'] = certificate_id
    time.sleep(5)
    for x in range(0, 3):
        try:
            retVal = cloudfront.update_distribution(DistributionConfig=distro.get('DistributionConfig'), Id=name, IfMatch=etag)
            break
        except ClientError as e:
            time.sleep(5)
    return retVal
