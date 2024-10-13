from odoo import fields, models

class CinemaComplex(models.Model):
    _name = 'cinema.cinema_complex'
    _description = 'A cinema complex containing auditoriums.'

    name = fields.Char(string='Cinema Complex Name')
    address = fields.Char(string='Address', required=True)
    auditorium_ids = fields.One2many('cinema.auditorium', 'cinema_id', string='Auditoriums')
