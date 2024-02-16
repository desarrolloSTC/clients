from odoo import models, fields

class client(models.Model):

	_inherit = 'res.partner'
	observaciones2 = fields.Char(string='Observaciones')