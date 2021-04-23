{
    'name': 'Engineer_as_a_service',
    'version': '1.0',
    'category': 'Trainee Demo',
    'sequence': 5,
    'summary': 'Trainee demo module',
    'depends': ['base'],

    'description': """
            module for trainee demo
            """,
            

    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/engineer.xml',
        'data/client.xml',
        'controllers/template.xml',
        'controllers/assests.xml',
    ],

    'application' : True

}