{
    'name': 'Gestión de Cursos',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/cursos_views.xml',
        'views/sesiones_views.xml',
    ],
    'application': True,
}