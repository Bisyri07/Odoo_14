from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    sale_type_id = fields.Many2one(comodel_name='sale.type', string='Sale Type')

    @api.model
    def create(self, vals):
        # Jika picking dibuat dari Sales Order
        if vals.get('origin'):
            sale_order = self.env['sale.order'].search([('name', '=', vals['origin'])], limit=1)
            if sale_order:
                vals['sale_type_id'] = sale_order.sale_type_id.id
        return super(StockPicking, self).create(vals)

    @api.onchange('origin')
    def _onchange_origin(self):
        if self.origin:
            sale_order = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
            if sale_order:
                self.sale_type_id = sale_order.sale_type_id