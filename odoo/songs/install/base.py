# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import os

def setup(ctx):
    """ Set Admin password """
    password = os.environ.get('ODOO_ADMIN_PASSWORD')
    if not password:
        raise Exception('Odoo password is missing')
    ctx.env['res.users'].search([]).write({
        'password': password,
        })
