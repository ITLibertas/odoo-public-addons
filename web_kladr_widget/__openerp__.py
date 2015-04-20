# -*- coding: utf-8 -*-
{
    'name': 'Web Kladr Widget',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Auto check and auto complete addresses by KLADR (FIAS)',
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
    'images': ['static/description/main.png'],
}
