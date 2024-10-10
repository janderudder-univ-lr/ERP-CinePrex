from odoo import fields, models

class Auditorium(models.Model):
    _name = 'cinema.auditorium'
    _description = 'An auditorium or screen in a cinema.'

    id = fields.Char(string='Auditorium Number or name', required=True)
    complex_id = fields.Many2one('cinema.cinema_complex', string='Cinema Complex')
    seat_ids = fields.One2many('cinema.seat', 'auditorium_id', string='Seats')
