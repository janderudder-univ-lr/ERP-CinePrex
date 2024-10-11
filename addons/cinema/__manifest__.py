{
    'name': 'Cinema',
    'version': '1.0',
    'depends': ['base'],
    'author': 'TotoEnF5',
    'category': 'Uncategorized',
    'description': 'A cinema',

    'installable': True,
    'application': True,

    'data': [
        'views/movie_views.xml',
        'views/movie_menus.xml',
        'security/ir.model.access.csv'
    ]
}