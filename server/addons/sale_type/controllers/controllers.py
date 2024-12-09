# -*- coding: utf-8 -*-
# from odoo import http


# class SaleType(http.Controller):
#     @http.route('/sale_type/sale_type/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_type/sale_type/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_type.listing', {
#             'root': '/sale_type/sale_type',
#             'objects': http.request.env['sale_type.sale_type'].search([]),
#         })

#     @http.route('/sale_type/sale_type/objects/<model("sale_type.sale_type"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_type.object', {
#             'object': obj
#         })
