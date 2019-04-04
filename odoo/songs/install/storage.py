import os
import anthem

def _configure_amazon_s3(ctx):
    with ctx.log("Configure Amazon S3 storage"):
        backend = ctx.env.ref('storage_backend.default_storage_backend')
        backend.write({
            'name': 'Amazon',
            'backend_type': 'amazon_s3',
            'aws_access_key_id': os.environ['STORAGE_AMAZON_KEY_ID'],
            'aws_secret_access_key': os.environ['STORAGE_AMAZON_ACCESS_KEY'],
            'aws_bucket': os.environ['STORAGE_AMAZON_BUCKET'],
            'aws_region': os.environ['STORAGE_AMAZON_REGION'],
            'base_url': os.environ['STORAGE_BASE_URL'],
            'directory_path': os.environ['STORAGE_DIR_PATH'],
            'served_by': 'external',
            })

@anthem.log
def setup(ctx):
    if os.environ.get('STORAGE_AMAZON_KEY_ID'):
        _configure_amazon_s3(ctx)


