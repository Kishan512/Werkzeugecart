from odoo import  fields, models

class Userslist(models.Model):
    _name = 'user.list'
    _description = "Engineers and Clients detail"

    # order_id = fields.Many2one('orders', string="orders")
    role = fields.Selection([('client', 'Client'), ('engineer', 'Engineer')], string="Role")
    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="mobile_no")
    password = fields.Char(string="password")
    address = fields.Char(string="Address")
    session = fields.Char(string="session")
    specialist = fields.Char(string="specialist")
    experience  = fields.Char(string="experience")
    # birthday = fields.Date(string="Birthday", required=True)
    # age = fields.Integer(compute="calculate_age", store=True)
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    # physics = fields.Integer()
    # chemistry = fields.Integer()
    # total = fields.Integer(string="Total")
    # average = fields.Float()
    # total_compute = fields.Integer(compute="_compute_total", store=True)
    # sem_fee = fields.Integer(string="Fee per semester")
    # enrollment_no = fields.Integer(string="Enrollment number")
    # branch = fields.Char(string="Branch")

class orders(models.Model):
    _name = 'orders'
    _description = "orders detail"

    # order_id = fields.Integer(string="order_id")
    engineer_id = fields.Many2one('user.list', string="engineer_id")
    client_id = fields.Many2one('user.list', string="client_id")
    # user_id = fields.One2many('user.list', 'id', string="user record")


