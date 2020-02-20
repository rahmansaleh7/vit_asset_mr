# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Catteg(models.Model):
    _name = 'stock.move'
    _inherit = 'stock.move'

    asset_cat_id = fields.Many2one(comodel_name='account.asset.category', string='Asset Category')

class ButtonValidate(models.Model):
    _name ='stock.picking'
    _inherit ='stock.picking'

    @api.multi
    def button_validate(self):
        res = super(ButtonValidate, self).button_validate()
        for obj in self.move_ids_without_package :
            vals = {
                'name': obj.product_id.name,
                'category_id': obj.asset_cat_id.id,
                'date': self.scheduled_date,
                'qty' : obj.product_uom_qty,
                'date_first_depreciation' : 'manual',
                'first_depreciation_manual_date' : obj.date_expected,
                'value': obj.product_id.standard_price * obj.product_uom_qty ,
                'unit_id' : self.unit_id.id,
                'analytic_tag_ids_l' : self.analytic_tag_ids.id,
                
            }
            self.env['account.asset.asset'].create(vals)

            
        return res