from odoo import  api,fields, models
import datetime

class student(models.Model):
    _name = 'student'
    _description = "student detail"

    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    image = fields.Binary(sting="image",attachment=True)
    gender = fields.Selection([('male','Male'),('female','Female')], default='male')
    birthday = fields.Date(string="DOB", required=True)
    age = fields.Char(compute="compute_age",store="True")
    # address = fields.Text(string="Address")
    collage_id = fields.Many2one('collage', string="collage")
    enrollment_no = fields.Integer(string="enrollment_no")
    mobile_no = fields.Char(string="mobile_no")
    hobbies = fields.Many2many('hobbies', string="hobies")   
    maths = fields.Integer(string="maths")
    physics = fields.Integer(string="physics")
    chemistry = fields.Integer(string="chemistry")
    total = fields.Integer(compute="comput_total",store=True)
    total_compute = fields.Integer(string="total")
    avg_marks = fields.Float(string="avg_marks") 

    # def custom_method_wizard(self):

    #     return {'type': 'ir.actions.act_window',
    #             'res_model': 'student.update',
    #             'view_mode': 'form',
    #             'target': 'new'}  
    @api.depends('birthday')
    def compute_age(self):
        today_date = datetime.date.today()
        for stud in self:
            if stud.birthday:
                birthday = fields.Datetime.to_datetime(stud.birthday).date()
                total_age = str(int((today_date - birthday).days / 365))
                stud.age = total_age
            else:
                stud.age =  "Birthdate is not provided..."

    @api.onchange('maths','physics','chemistry')
    def comput_marks(self):
        for res in self:
            res.total_compute=res.maths + res.physics + res.chemistry
            res.avg_marks=res.total_compute / 3
        

    @api.depends('maths','physics','chemistry')
    def comput_total(self):
        for rec in self:
            rec.total=rec.maths + rec.physics + rec.chemistry
            rec.avg_marks = rec.total/3

class collage(models.Model):
    _name = 'collage'
    _description = "collage detail"

    name = fields.Char(string="Name")
    city = fields.Char(string="City")
    students = fields.One2many('student', 'collage_id', string='Terms')


class hobbies(models.Model):
    _name = 'hobbies'
    _description = "hobbies of studets"

    name = fields.Char(string="Name")

class student_address(models.Model):
    _inherit = 'student'
    _description = "student address inherit"

    house_no = fields.Integer(string="House No")
    street = fields.Char(string="Street")
    area = fields.Char(string="area")
    city = fields.Char(string="city")
    zip_code = fields.Integer(string="zip_code")