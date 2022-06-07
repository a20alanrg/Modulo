from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name="hospital.doctor"
    _description="Hospital Doctor"

    name=fields.Char(string='Name', required=True)
    age=fields.Integer(string='Age')
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ],required=True,default='other')
    patients=fields.Integer(string="Patients", compute="patients_count")

    def patients_count(self):
        count=self.env["hospital.patient"].search_count([("doctor_id","=",self.id)])
        self.patients=count