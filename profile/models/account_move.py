# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_new_customer = fields.Boolean(
        string='Is new customer',
        readonly=True,
    )
