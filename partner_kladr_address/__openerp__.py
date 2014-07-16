{
    'name': 'KLADR address',
    'version': '0.2',
    'category' : 'Sales Management',
    'description': """
Format address in Russian KLADR for partner form
""",
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': ['base', 'web_kladr_widget'],
    'data': [
           'res_partner_view.xml',
           'res_bank_view.xml',
    ],
    'installable': True,
    'images': [],
}