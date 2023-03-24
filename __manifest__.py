{
    'name': "POS Discount",
    'version': "16.0.1.0.0",
    'sequence': -21,
    'summary': 'POS',
    'author': 'CYBROSYS',
    'installable': True,
    'application': True,

    'depends': ['base', 'point_of_sale'],

    'data': ['views/pos_settings.xml'],
    'assets': {
        'point_of_sale.assets': [
            'pos_discount_limit/static/src/js/discount.js',

        ],

    },
}
