{
    'name': 'Gestión de Cursos',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cursos_views.xml',
        'views/sesiones_views.xml',
        'views/menu.xml',
    ],
    'application': True,
}