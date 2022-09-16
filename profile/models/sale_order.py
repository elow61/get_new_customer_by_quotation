# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_new_customer = fields.Boolean(
        string='Is new customer',
        readonly=True
    )

    @api.model
    def create(self, vals):
        partner = self.env['res.partner'].browse(vals.get('partner_id'))
        if not partner.sale_order_ids:
            vals['is_new_customer'] = True
        result = super(SaleOrder, self).create(vals)
        return result

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({'is_new_customer': self.is_new_customer})
        return invoice_vals
