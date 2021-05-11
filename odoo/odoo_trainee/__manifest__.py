{
    'name': 'odoo_trainee',
    'version': '1.0',
    'category': 'Trainee Demo',
    'sequence': 5,
    'summary': 'Trainee demo module',
    'depends': ['base'],

    'description': """
            module for trainee demo
            """,
            

    'data' : [
        'security/ir.model.access.csv',
        # 'data/data.xml',
        'wizard/student_update_wizard_view.xml',
        'views/home.xml',
        'reports/Student_report.xml',
    ],

    'application' : True

}