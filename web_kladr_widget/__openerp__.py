# -*- coding: utf-8 -*-
{
    'name': 'web_kladr_widget',
    'version': '0.1',
    'category': 'Tools',
    'description': """
Web KLADR Custom Widget
auto check and autocomplete address
""",
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': ['web'],
    'data' : [ 
		'views/web_kladr_widget.xml',
	],
    'js': [
       # 'static/src/js/jquery.primepix.kladr.min.js',
	#'static/src/js/web_kladr_widget.js',
    ],
    'css': [
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'images': [],
}
