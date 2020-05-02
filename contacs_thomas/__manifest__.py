# -*- coding: utf-8 -*-
{
    'name': "Contacs Thomas",

    'summary': "Contacs Thomas",

    'description': "Contacs Thomas",

    'author': "Todoo SAS",
    'contributors': ['Fernando Fernandez nf@todoo.co'],
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['crm','website','base_address_city'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/res_partner_view.xml',
        'views/crm_lead_view.xml',
        'views/mail_template.xml',
        'views/templates.xml',
        'wizard/crm_lead_lost_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
