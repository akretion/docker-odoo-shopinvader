import os
import anthem

@anthem.log
def setup(ctx):
    backend = ctx.env.ref('shopinvader.backend_1')
    backend.elasticsearch_server_ip = 'elastic'
    bindings = ctx.env['shopinvader.variant'].search([])
    bindings.recompute_json(force_export=True)
    bindings = ctx.env['shopinvader.category'].search([])
    bindings.recompute_json(force_export=True)
