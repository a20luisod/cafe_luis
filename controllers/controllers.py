# -*- coding: utf-8 -*-
# from odoo import http


# class CafeLuis(http.Controller):
#     @http.route('/cafe_luis/cafe_luis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cafe_luis/cafe_luis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cafe_luis.listing', {
#             'root': '/cafe_luis/cafe_luis',
#             'objects': http.request.env['cafe_luis.cafe_luis'].search([]),
#         })

#     @http.route('/cafe_luis/cafe_luis/objects/<model("cafe_luis.cafe_luis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cafe_luis.object', {
#             'object': obj
#         })
