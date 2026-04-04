{
    # App Information
    'name': 'Chatter Message Clear',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Clear all chatter messages from a record with confirmation(Delete chatter message, Chatter Message Clear, clear chatter, Remove log note, Delete message from chatter, Odoo chatter delete, Chatter message delete, Delete chatter history, Remove chatter message, Delete log note, Clear record discussion, Delete record messages, Chatter clear, Chatter cleaner)',
    'description': """
    Chatter Message Clear
    =====================
    
    Adds a clear action in the backend chatter to delete all messages from the
    current record after an explicit confirmation.
    """,
    'category': 'Productivity',

    # Author
    'author': 'Techno Stellar',
    'maintainer': 'Techno Stellar',

    # dependencies
    'depends': ['mail', 'web'],

    # Views & Data
    'data': [
        'security/security.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'chatter_message_clear_tspl/static/src/js/chatter_clear_patch.js',
            'chatter_message_clear_tspl/static/src/xml/chatter_clear_button.xml',
        ],
    },

    # Technical
    'images': ['static/description/banner_v18.png',],
    'installable': True,
    'application': False,
    'auto_install': False,

    # Pricing
    'price': 0.0,
    'currency': 'EUR',
}
