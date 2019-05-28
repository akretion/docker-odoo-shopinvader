import os
import anthem

@anthem.log
def setup(ctx):
    backend = ctx.env.ref('shopinvader_elasticsearch.shopinvader.backend_1')
    backend.elasticsearch_server_ip = 'elastic'
