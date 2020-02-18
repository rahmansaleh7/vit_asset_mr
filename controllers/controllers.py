# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetMr(http.Controller):
#     @http.route('/vit_asset_mr/vit_asset_mr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_asset_mr/vit_asset_mr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_asset_mr.listing', {
#             'root': '/vit_asset_mr/vit_asset_mr',
#             'objects': http.request.env['vit_asset_mr.vit_asset_mr'].search([]),
#         })

#     @http.route('/vit_asset_mr/vit_asset_mr/objects/<model("vit_asset_mr.vit_asset_mr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_asset_mr.object', {
#             'object': obj
#         })