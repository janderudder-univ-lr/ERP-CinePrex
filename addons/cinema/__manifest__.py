{
    'name': 'Cineprex',
    'version': '1.0',
    'depends': ['base'],
    'author': 'TotoEnF5',
    'category': 'Uncategorized',
    'description': 'Truly one of the cinema complexes of all time',

    'installable': True,
    'application': True,

    'data': [
        'views/movie_views.xml',
        'views/movie_menus.xml',
        'security/ir.model.access.csv'
    ]
}