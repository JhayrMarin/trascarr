# -*- coding: utf-8 -*-
# from odoo import http


# class UmgGrupo2(http.Controller):
#     @http.route('/umg_grupo2/umg_grupo2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/umg_grupo2/umg_grupo2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('umg_grupo2.listing', {
#             'root': '/umg_grupo2/umg_grupo2',
#             'objects': http.request.env['umg_grupo2.umg_grupo2'].search([]),
#         })

#     @http.route('/umg_grupo2/umg_grupo2/objects/<model("umg_grupo2.umg_grupo2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('umg_grupo2.object', {
#             'object': obj
#         })
