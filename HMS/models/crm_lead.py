from odoo import models, fields, api
from odoo.exceptions import UserError


class patient_customer(models.Model):
    _inherit = 'crm.lead'

    related_patient_id = fields.Integer()

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise UserError(f"You can't delete this customer as he is a patient")
        super().unlink()
