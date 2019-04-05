import os
import anthem
import requests
API = 'https://loripsum.net/api/'

def loremsum(nbr, size):
    return requests.get('https://loripsum.net/api/%s/%s' % (nbr, size)).text

@anthem.log
def setup(ctx):
    env = ctx.env
    backend = env.ref('shopinvader.backend_1')
    backend.write({
        'auth_api_key_name': 'api_key_shopinvader_demo'
        })
    countries = env['res.country'].search([])
    backend.write({
        'allowed_country_ids': [(6, 0, countries.ids)],
        'category_binding_level': 3,
        })
    products = env['product.product'].search([
        ('image_ids', '!=', False),
        ])
    wizard = env['shopinvader.variant.binding.wizard'].create({
        'backend_id': backend.id,
        'product_ids': [(6, 0, products.ids)],
        })
    wizard.bind_products()
    for binding in env['shopinvader.product'].search([]):
        binding.write({
            'description': loremsum('3', 'medium'),
            'short_description': loremsum('1', 'short'),
            })
