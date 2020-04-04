from odoo import models, fields, api
from odoo.exceptions import UserError


class patient_customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(comodel_name="hms.patient")
    vat = fields.Char(required=True)



    # @api.constrain('email')
    # def check_email(self):
    #     for rec in self:
    #         if rec.related_patient_id:
    #             patient_email = rec.related_patient_id.email
    #             if rec.search(['email', '=', patient_email]):
    #                 raise UserError(f'change your email please')

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise UserError(f"You can't delete this customer as he is a patient")
        super().unlink()
