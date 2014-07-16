{
    'name': 'CRM KLADR',
    'version': '0.2',
    'category' : 'Sales Management',
    'description': """
Format address in Russian KLADR for CRM lead
""",
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': ['base', 'web_kladr_widget','crm'],
    'data': [
           'crm_lead.xml',
    ],
    'installable': True,
    'images': [],
}