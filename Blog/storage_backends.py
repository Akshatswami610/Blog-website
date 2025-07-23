# Blog/storage_backends.py
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'  # All uploaded files will go under 'media/' folder in S3
    default_acl = 'public-read'
