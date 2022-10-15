# -*- coding: utf-8 -*-
import base64
from email.policy import default
from multiprocessing import set_forkserver_preload
from odoo.exceptions import UserError

from odoo import api, fields, models, _
from odoo import tools


class UmgGrupo2(models.TransientModel):
    _name = "umg_grupo2.grupo2.wizard"
    _description = "Wizard integrantes del grupo 2 UMG"

    integrantes = fields.Html(string='Integrantes')

    def _build_contexts(self, data):
        result = {}
        result['integrantes'] = data['form']['integrantes'] or False
        return result