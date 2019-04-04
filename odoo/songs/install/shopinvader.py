import os
import anthem

@anthem.log
def setup(ctx):
    backend = ctx.env.ref('shopinvader.backend_1')
    backend.write({
        'auth_api_key_name': 'api_key_shopinvader_demo'
        })
