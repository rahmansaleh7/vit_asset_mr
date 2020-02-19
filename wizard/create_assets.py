from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare


class CreateAssetStock(models.TransientModel):
    _name = 'create.asset.stock'
    _description = 'Create Asset'

    pick_ids = fields.Many2many('stock.picking', 'stock_picking_backorder_rel')

    @api.one
    def _process(self, cancel_backorder=False):
        if cancel_backorder:
            for pick_id in self.pick_ids:
                moves_to_log = {}
                for move in pick_id.move_lines:
                    if float_compare(move.product_uom_qty, move.quantity_done, precision_rounding=move.product_uom.rounding) > 0:
                        moves_to_log[move] = (move.quantity_done, move.product_uom_qty)
                pick_id._log_less_quantities_than_expected(moves_to_log)
        self.pick_ids.action_done()
        if cancel_backorder:
            for pick_id in self.pick_ids:
                backorder_pick = self.env['stock.picking'].search([('backorder_id', '=', pick_id.id)])
                backorder_pick.action_cancel()
                pick_id.message_post(body=_("Back order <em>%s</em> <b>cancelled</b>.") % (",".join([b.name or '' for b in backorder_pick])))

    def process(self):
        self._process()

    def process_cancel_backorder(self):
        self._process(cancel_backorder=True)
