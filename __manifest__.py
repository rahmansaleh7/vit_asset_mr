# -*- coding: utf-8 -*-
{
    'name': "vit_asset_mr",

    'summary': """
                Modul Penambahan Create Asset dan Asset Category""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Iqbal Abdurrahman",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'stock',
                'om_account_accountant',
                'om_account_asset',
                'vit_unit_location',
                # 'vit_asset',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'wizard/create_assets.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}