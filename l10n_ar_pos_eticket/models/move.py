# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_move_vals(self):
        nombre = self.name.split(" ")
        numero = nombre[1] if len(nombre) > 1 else nombre[0]
        letra = nombre[0]
        return {
            'l10n_ar_afip_auth_code': self.l10n_ar_afip_auth_code,
            'l10n_ar_afip_qr_code': self.l10n_ar_afip_qr_code,
            'l10n_ar_afip_auth_code_due': self.l10n_ar_afip_auth_code_due,
            'invoice_date_due': self.invoice_date_due,
            'l10n_latam_document_type_id': self.l10n_latam_document_type_id.name,

            'l10n_ar_afip_start_date': self.company_id.l10n_ar_afip_start_date,
            'l10n_ar_gross_income_number': self.company_id.l10n_ar_gross_income_number,
            'street': self.company_id.street,
            'city': self.company_id.city,

            'invoice_id': self.id,
            'invoice_number': numero,
            'invoice_letter': letra,
            
            'qr_code_img': '/report/barcode/?barcode_type=%s&value=%s&width=%s&height=%s' % ('QR', self.l10n_ar_afip_qr_code, 180, 180)
        }