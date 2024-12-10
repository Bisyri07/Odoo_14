from odoo import models, fields, api


class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	discount_amount = fields.Float(string="Discount Amount",
	                               compute="_compute_discount_amount",
	                               store=True)

	@api.depends('discount', 'price_unit', 'product_uom_qty')
	def _compute_discount_amount(self):
		for line in self:
			line.discount_amount = line.price_unit * line.product_uom_qty * (line.discount / 100)

