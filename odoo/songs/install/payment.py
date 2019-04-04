import os
import anthem

def _configure_stripe(ctx):
    with ctx.log("Configure Stripe Payment"):
        ctx.env['keychain.account'].create({
            'name': 'Stripe',
            'technical_name': 'stripe',
            'namespace': 'stripe',
            'environment': 'dev',
            'password': os.environ['STRIPE_API_KEY'],
            })

@anthem.log
def setup(ctx):
    if os.environ.get('STRIPE_API_KEY'):
        _configure_stripe(ctx)
