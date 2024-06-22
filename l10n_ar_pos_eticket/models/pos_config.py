# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = 'pos.config'
    print_pdf_invoice = fields.Boolean('Print PDF Invoice', default=1)
    pos_auto_invoice = fields.Boolean('POS auto invoice',
                                      help='POS auto to checked to invoice button',
                                      default=1)
    receipt_invoice_number = fields.Boolean('Receipt show invoice number', default=1)
    receipt_customer_vat = fields.Boolean('Receipt show customer VAT', default=1)
    partner_default = fields.Many2one("res.partner", string="Cliente Por defecto")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    print_pdf_invoice = fields.Boolean(related='pos_config_id.print_pdf_invoice', readonly=False)
    pos_auto_invoice = fields.Boolean(related='pos_config_id.pos_auto_invoice', readonly=False)
    receipt_invoice_number = fields.Boolean(related='pos_config_id.receipt_invoice_number', readonly=False)
    receipt_customer_vat = fields.Boolean(related='pos_config_id.receipt_customer_vat', readonly=False)
    partner_default = fields.Many2one('res.partner', string='Partner default', related='pos_config_id.partner_default',
                                      readonly=False)
