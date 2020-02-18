from odoo import models, fields, api, _

class CreateAssets(models.TransientModel):
    _name = 'vit_assets_mrp.createassets'

    asset_cat = fields.Many2one(commodel_name='account.asset.category', string='Asset Category')
    assetscat_ids = fields.One2many(comodel_name='vit_assets_mrp.createassets.assets', inverse_name='wizard_id', string='Add Assets')

class AssetsAssets(models.TransientModel):
    _name = 'vit_assets_mrp.createassets.assets'

    wizard_id = fields.Many2one(comodel_name='vit_assets_mrp.createassets' , string='Wizard')
    assets_ids = fields.Many2one(comodel_name='om_account_accountant.account.asset.asset', string='Add Assets')