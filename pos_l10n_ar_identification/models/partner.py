# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains('vat', 'l10n_latam_identification_type_id')
    def check_vat(self):
        """ Since we validate more documents than the vat for Argentinian partners (CUIT - VAT AR, CUIL, DNI) we
        extend this method in order to process it. """
        # NOTE by the moment we include the CUIT (VAT AR) validation also here because we extend the messages
        # errors to be more friendly to the user. In a future when Odoo improve the base_vat message errors
        # we can change this method and use the base_vat.check_vat_ar method.s
        type_id = int(self.l10n_latam_identification_type_id.id)
        l10n_ar_partners = self.filtered(lambda self: self.env['l10n_latam.identification.type'].browse(type_id).l10n_ar_afip_code)
        l10n_ar_partners.l10n_ar_identification_validation()
        return super(ResPartner, self - l10n_ar_partners).check_vat()


class Session(models.Model):
    _inherit = "pos.session"

    @api.model
    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('l10n_ar.afip.responsibility.type')
        res.append('l10n_latam.identification.type')
        return res

    def _get_pos_ui_l10n_ar_afip_responsibility_type(self, params):
        return self.env['l10n_ar.afip.responsibility.type'].search_read(**params['search_params'])

    def _loader_params_l10n_ar_afip_responsibility_type(self):
        return {'search_params': {'domain': [], 'fields': []}}

    def _get_pos_ui_l10n_latam_identification_type(self, params):
        return self.env['l10n_latam.identification.type'].search_read(**params['search_params'])

    def _loader_params_l10n_latam_identification_type(self):
        return {'search_params': {'domain': [], 'fields': []}}

    def _loader_params_res_partner(self):
        return {
            'search_params': {
                'domain': [],
                'fields': [
                    'name', 'street', 'city', 'state_id', 'country_id', 'vat', 'lang', 'phone', 'zip', 'mobile', 'email',
                    'barcode', 'write_date', 'property_account_position_id', 'property_product_pricelist', 'parent_name',
                    'l10n_ar_afip_responsibility_type_id', 'l10n_latam_identification_type_id'
                ],
            },
        }