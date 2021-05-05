from odoo import  fields, models

class student(models.Model):
    _name = 'student'
    _description = "student detail"

    collage_id = fields.Many2one('collage', string="collage")
    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="mobile_no")
    gender = fields.Selection([('male','Male'),('female','Female')], default='male')
    birthday = fields.Date(string="DOB", required=True)
    password = fields.Char(string="password")
    address = fields.Text(string="Address")      

class collage(models.Model):
    _name = 'collage'
    _description = "collage detail"

    name = fields.Char(string="Name")
    city = fields.Char(string="City")
    students = fields.One2many('student', 'collage_id', string='Terms')

