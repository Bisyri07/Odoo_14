from odoo import models, fields, api


class AccoutMove(models.Model):
	_inherit = "account.move"

	sale_type_id = fields.Many2one(comodel_name='sale.type', string='Sale Type')

	@api.model
	def create(self, vals):
		# Jika invoice dibuat dari Sales Order
		if vals.get('invoice_origin'):
			sale_order = self.env['sale.order'].search([('name', '=', vals['invoice_origin'])], limit=1)
			if sale_order:
				vals['sale_type_id'] = sale_order.sale_type_id.id
		return super(AccountMove, self).create(vals)

	@api.onchange('invoice_origin')
	def _onchange_invoice_origin(self):
		if self.invoice_origin:
			sale_order = self.env['sale.order'].search([('name', '=', self.invoice_origin)], limit=1)
			if sale_order:
				self.sale_type_id = sale_order.sale_type_id

