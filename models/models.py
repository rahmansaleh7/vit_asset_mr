# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Catteg(models.Model):
    _name = 'stock.move'
    _inherit = 'stock.move'

    asset_cat = fields.Many2one(commodelname='account.asset.category', string='Asset Category')

class ButtonValidate(models.Model):
    _name ='stock.picking'
    _inherit ='stock.picking'

    asset_idx =fields.Many2one(comodelname='account.asset.asset', string='Name Assets')

    def button_validate(self):
        print("================================================================")
