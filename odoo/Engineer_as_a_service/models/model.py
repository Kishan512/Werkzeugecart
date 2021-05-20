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
    rating = fields.Integer(string="rating")
 
class service(models.Model):
    _name = 'service'
    _description = "service detail"

    name = fields.Char(string="Name")
    


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
    order_status = fields.Integer(string="status")
    # user_id = fields.One2many('user.list', 'id', string="user record")


class job_work_detail(models.Model):
    _name = 'job_work_detail'
    _description = "orders/job detail"

    order_id = fields.Many2one('orders', string="order_id")
    product_name = fields.Char(string="product_name")
    product_problem = fields.Char(string="product_problem")
    job_address = fields.Char(string="job_address")
    


class ratings(models.Model):
    _name = 'ratings'
    _description = "Ratings of Engineers"

    engineer_id = fields.Many2one('engineer', string="engineer_id")
    client_id = fields.Many2one('client', string="client_id")
    order_id = fields.Many2one('orders', string="order_id")
    rating = fields.Integer(string="rating")
    feedback = fields.Char(string="feedback")


    def cal_rating(self):
        count = len(self)
        if count == 0:
            return 0
        else:    
            sum = 0
            for rid in self:
                sum =sum + rid.rating
            rating=sum/count
            return rating
