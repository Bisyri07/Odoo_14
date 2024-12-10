from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(string='Discount Amount')

    @api.onchange('discount_amount', 'quantity', 'price_unit')
    def _onchange_discount_amount(self):
        for line in self:
            # Hitung ulang nilai debit/credit dengan memperhitungkan discount_amount
            line.debit = max(0, (line.price_unit * line.quantity) - line.discount_amount)
            line.credit = max(0, (line.price_unit * line.quantity) - line.discount_amount)
