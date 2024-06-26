# sale_order_custom_price/models/sale_order_line.py
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    modified_price = fields.Float(string="Modified Price", readonly=True, store=True)

    @api.model
    def create(self, vals):
        if 'price_unit' in vals:
            vals['modified_price'] = vals['price_unit']
        return super(SaleOrderLine, self).create(vals)

    @api.onchange('product_uom_qty', 'product_id', 'order_id.pricelist_id')
    def _onchange_product_id(self):
        super(SaleOrderLine, self)._onchange_product_id()
        if self.order_id.pricelist_id and self.product_id:
            if self.modified_price and self.modified_price != self.product_id.lst_price:
                # Use the modified price as the base price
                base_price = self.modified_price
            else:
                base_price = self.product_id.lst_price

            # Apply the pricelist to the base price
            price = self.order_id.pricelist_id.get_product_price(
                self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id)
            self.price_unit = price if price != self.product_id.lst_price else base_price

    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        self.modified_price = self.price_unit
