from odoo import models, fields

class client(models.Model):

	_inherit = 'res.partner'

	observaciones = fields.Char(string='Observaciones')


