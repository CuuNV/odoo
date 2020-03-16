# -*- coding: utf-8 -*-
{
    'name': 'User Shortcut Menu',
    'price': 0.0,
    'category': 'Extra Tools',
    'license': 'AGPL-3',
    'currency': 'EUR',
    'version': '12.0.1',
    'author': 'CuuNV',
    'maintainer': 'CuuNV <nguyenvancuu.vp@gmail.com>',
    'website': '',
    'description': """
    Shortcut menu
    =============
    Allow user add list of frequently used menu items and display in a systray item
    """,
    'depends': [
        'base',
        'web'
    ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'qweb': [
        'static/src/xml/templates.xml'
    ],
    'installable': True,
    'auto_install': False,
}
