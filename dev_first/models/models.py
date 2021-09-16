# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner_inherit(models.Model):
    _inherit = 'res.partner'
    _description = 'inherit partner for user...!'

    name_mother = fields.Char()
    value2 = fields.Float(compute="_value_pc", store=True)
    value = fields.Integer()
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    


# class dev_first(models.Model):
#     _name = 'dev_first.dev_first'
#     _description = 'dev_first.dev_first'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
