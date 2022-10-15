# -*- coding: utf-8 -*-
{
    'name': "umg_grupo2",

    'summary': """
        Trascarr 2022""",

    'description': """
        Entrega de proyecto por parte del grupo #2 de la Universidad Mariano Gálvez de Guatemala.
        Integrantes:
            NERY RODOLFO SINAY MATEO 5390 18 22939\n
            CRISTOFER ISRAEL DE LEÓN SANTOS 5390 06 2060\n
            HORACIO LORENZO BAMACA DIAZ 5390 17 6440\n
            JHAYR SCOTT MARIN RIVERA 5390 17 1398\n
        """,

    'author': "Grupo2",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/umg_grupo2_wizard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
