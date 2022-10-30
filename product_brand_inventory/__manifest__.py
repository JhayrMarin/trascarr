# -*- coding: utf-8 -*-
{
    'name': 'Marcas de productos',
    'version': '13.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Brand in Inventory',
    'author': 'UMG',
    'company': 'UMG',
    'maintainer': 'Jhayr Marin',
    'images': ['static/description/banner.png'],
    'website': 'https://www.example.com',
    'depends': ['stock'],
    'data': [
        'views/brand_views.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
