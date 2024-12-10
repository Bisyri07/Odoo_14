from odoo import models, fields


class GeneralSaleReport(models.Model):
    _name = 'general.sale.report'
    _auto = False
    _description = 'General Sale Report'

    product_id = fields.Many2one('product.product', string='Product Name')
    default_code = fields.Char(string='Product Internal Reference')
    product_category_id = fields.Many2one('product.category', string='Product Category')
    order_id = fields.Many2one('sale.order', string='Sale Order')
    picking_id = fields.Many2one('stock.picking', string='Delivery Order')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    sale_type_id = fields.Many2one('sale.type', string='Sale Type')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Price')
    discount = fields.Float(string='Discount (%)')
    discount_amount = fields.Float(string='Discount Amount')
    price_subtotal = fields.Float(string='Subtotal')
    payment_term_id = fields.Many2one('account.payment.term', string='Payment Terms')
    payment_date = fields.Date(string='Payment Date')
    invoice_payment_state = fields.Selection([
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
    ], string='Invoice Payment Status')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW general_sale_report AS (
                SELECT
                    sol.id AS id,
                    sol.product_id AS product_id,
                    pp.default_code AS default_code,
                    pt.categ_id AS product_category_id,
                    sol.order_id AS order_id,
                    sp.id AS picking_id,
                    am.id AS invoice_id,
                    so.sale_type_id AS sale_type_id,
                    sol.product_uom_qty AS quantity,
                    sol.price_unit AS price_unit,
                    sol.discount AS discount,
                    sol.discount_amount AS discount_amount,
                    sol.price_subtotal AS price_subtotal,
                    so.payment_term_id AS payment_term_id,
                    COALESCE(
                        (SELECT MAX(ap.payment_type)
                         FROM account_payment ap
                         WHERE ap.move_id = am.id),
                        NULL
                    ) AS payment_date,
                    am.payment_state AS invoice_payment_state
                FROM
                    sale_order_line sol
                JOIN sale_order so ON sol.order_id = so.id
                LEFT JOIN stock_picking sp ON sp.origin = so.name
                LEFT JOIN account_move am ON am.invoice_origin = so.name
                LEFT JOIN product_product pp ON sol.product_id = pp.id
                LEFT JOIN product_template pt ON pp.product_tmpl_id = pt.id
                WHERE am.state = 'posted'
        )
        """)

