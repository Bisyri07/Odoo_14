from odoo import models, fields, api


class SaleOrder(models.Model):
	_inherit = "sale.order"

	sale_type_id = fields.Many2one(comodel_name='sale.type', string='Sale Type')

	def _prepare_invoice_line(self, line):
		res = super(SaleOrder, self)._prepare_invoice_line(line)
		res.update({
			'discount_amount': line.discount_amount,
		})
		return res

	@api.depends('order_line.price_subtotal')
	def _compute_amount(self):
		super(SaleOrder, self)._compute_amount()
		for order in self:
			additional_discount = sum(order.order_line.mapped('discount_amount'))
			order.amount_total -= additional_discount


