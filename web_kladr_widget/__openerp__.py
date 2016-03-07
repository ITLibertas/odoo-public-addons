# -*- coding: utf-8 -*-
{
    'name': 'Web Kladr Widget',
    'version': '1.5',
    'category': 'Tools',
    'summary': 'KLADR/FIAS addresses auto complete',
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
