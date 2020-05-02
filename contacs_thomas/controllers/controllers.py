# -*- coding: utf-8 -*-
# from odoo import http


# class ContacsEnlanube(http.Controller):
#     @http.route('/contacs_thomas/contacs_thomas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacs_thomas/contacs_thomas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacs_thomas.listing', {
#             'root': '/contacs_thomas/contacs_thomas',
#             'objects': http.request.env['contacs_thomas.contacs_thomas'].search([]),
#         })

#     @http.route('/contacs_thomas/contacs_thomas/objects/<model("contacs_thomas.contacs_thomas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacs_thomas.object', {
#             'object': obj
#         })
