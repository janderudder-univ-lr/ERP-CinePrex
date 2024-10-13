from odoo import fields, models

class Seat(models.Model):
    _name = 'cinema.seat'
    _description = 'Seat'

    row = fields.Char(string='Seat Row')
    number = fields.Integer(string='Seat Number')
    auditorium_id = fields.Many2one('cinema.auditorium', string='Auditorium')
