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

        # print("================================================================")

    # vals = {
    #     'amount': amount,
    #     'asset_id': self.id,
    #     'sequence': sequence,
    #     'name': (self.code or '') + '/' + str(sequence),
    #     'remaining_value': residual_amount,
    #     'depreciated_value': self.value - (self.salvage_value + residual_amount),
    #     'depreciation_date': depreciation_date,
    # }
    # commands.append((0, False, vals))

    @api.multi
    def button_validate(self):
        self.ensure_one()
        # if not self.move_lines and not self.move_line_ids:
        #     raise UserError(_('Please add some items to move.'))

        # # If no lots when needed, raise error
        # picking_type = self.picking_type_id
        # precision_digits = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        # no_quantities_done = all(float_is_zero(move_line.qty_done, precision_digits=precision_digits) for move_line in self.move_line_ids.filtered(lambda m: m.state not in ('done', 'cancel')))
        # no_reserved_quantities = all(float_is_zero(move_line.product_qty, precision_rounding=move_line.product_uom_id.rounding) for move_line in self.move_line_ids)
        # if no_reserved_quantities and no_quantities_done:
        #     raise UserError(_('You cannot validate a transfer if no quantites are reserved nor done. To force the transfer, switch in edit more and encode the done quantities.'))

        # if picking_type.use_create_lots or picking_type.use_existing_lots:
        #     lines_to_check = self.move_line_ids
        #     if not no_quantities_done:
        #         lines_to_check = lines_to_check.filtered(
        #             lambda line: float_compare(line.qty_done, 0,
        #                                        precision_rounding=line.product_uom_id.rounding)
        #         )

        #     for line in lines_to_check:
        #         product = line.product_id
        #         if product and product.tracking != 'none':
        #             if not line.lot_name and not line.lot_id:
        #                 raise UserError(_('You need to supply a Lot/Serial number for product %s.') % product.display_name)

        # if no_quantities_done:
        #     view = self.env.ref('stock.view_immediate_transfer')
        #     wiz = self.env['stock.immediate.transfer'].create({'pick_ids': [(4, self.id)]})
        #     return {
        #         'name': _('Immediate Transfer?'),
        #         'type': 'ir.actions.act_window',
        #         'view_type': 'form',
        #         'view_mode': 'form',
        #         'res_model': 'stock.immediate.transfer',
        #         'views': [(view.id, 'form')],
        #         'view_id': view.id,
        #         'target': 'new',
        #         'res_id': wiz.id,
        #         'context': self.env.context,
        #     }

        # if self._get_overprocessed_stock_moves() and not self._context.get('skip_overprocessed_check'):
        #     view = self.env.ref('stock.view_overprocessed_transfer')
        #     wiz = self.env['stock.overprocessed.transfer'].create({'picking_id': self.id})
        #     return {
        #         'type': 'ir.actions.act_window',
        #         'view_type': 'form',
        #         'view_mode': 'form',
        #         'res_model': 'stock.overprocessed.transfer',
        #         'views': [(view.id, 'form')],
        #         'view_id': view.id,
        #         'target': 'new',
        #         'res_id': wiz.id,
        #         'context': self.env.context,
        #     }

        # Check backorder should check for other barcodes
        if self._check_backorder():
            return self.action_generate_backorder_wizard()
        self.action_done()
        return


    def action_generate_backorder_wizard(self):
        # print("================================================================")
        res = super(ButtonValidate, self).action_generate_backorder_wizard()
            # ass = self.env['account.asset.asset'].search([('origin','=', ass.name)])
            # asset = super(ButtonValidate, self.with_context(mail_create_nolog=True)).create(self.account.asset.asset)
        return res