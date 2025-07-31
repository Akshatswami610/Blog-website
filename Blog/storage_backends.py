from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def get_object_parameters(self, name):
        params = super().get_object_parameters(name)
        params['ACL'] = 'public-read'
        return params
