from odoo import  fields, models

class engineer(models.Model):
    _name = 'engineer'
    _description = "Engineers detail"

    # order_id = fields.Many2one('orders', string="orders")
    role = fields.Selection([('engineer', 'Engineer')], string="Role")
    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="mobile_no")
    password = fields.Char(string="password")
    address = fields.Char(string="Address")           
    specialist = fields.Char(string="specialist")
    experience  = fields.Char(string="experience")
 

class client(models.Model):
    _name = 'client'
    _description = "Clients detail"

    # order_id = fields.Many2one('orders', string="orders")
    role = fields.Selection([('client', 'Client')], string="Role")
    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="mobile_no")
    password = fields.Char(string="password")
    address = fields.Char(string="Address")           


class orders(models.Model):
    _name = 'orders'
    _description = "orders detail"

    # order_id = fields.Integer(string="order_id")
    engineer_id = fields.Many2one('engineer', string="engineer_id")
    client_id = fields.Many2one('client', string="client_id")
    # user_id = fields.One2many('user.list', 'id', string="user record")


