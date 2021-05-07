from odoo import  api,fields, models



class student_update(models.TransientModel):
    _name = 'student.update'
    _description = "student_update "

    collage_id = fields.Many2one("collage",string="collage_id")


    def update_student(self):
    	self.env['student'].browse(self._context.get("active_ids")).update({"collage_id":self.collage_id})
    	return True