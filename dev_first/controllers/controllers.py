# -*- coding: utf-8 -*-
# from odoo import http


# class DevFirst(http.Controller):
#     @http.route('/dev_first/dev_first/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_first/dev_first/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_first.listing', {
#             'root': '/dev_first/dev_first',
#             'objects': http.request.env['dev_first.dev_first'].search([]),
#         })

#     @http.route('/dev_first/dev_first/objects/<model("dev_first.dev_first"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_first.object', {
#             'object': obj
#         })
