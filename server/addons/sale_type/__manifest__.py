# -*- coding: utf-8 -*-
{
    'name': "sale_type",
    'summary': """Modul untuk mengelola Jenis Penjualan""",
    'description': """
        Long description of module's purpose
    """,

    'author': "Bisyri",
    'website': "http://www.yourcompany.com",
    'application':True,
    'sequence': 5,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_type_view.xml',
        'views/main_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
