{
    'name': 'CRM KLADR',
    'version': '1.4',
    'category' : 'Sales Management',
    'summary': 'KLADR/FIAS addresses auto complete on a lead form',
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': ['base', 'web_kladr_widget','crm'],
    'data': [
           'crm_lead.xml',
    ],
    'installable': True,
    'images': ['static/description/main.png'],
}
