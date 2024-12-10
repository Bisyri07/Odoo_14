from odoo import models, fields


class SaleOrder(models.Model):
	_inherit = "sale.order"

	sale_type_id = fields.Many2one(comodel_name='sale.type', string='Sale Type')