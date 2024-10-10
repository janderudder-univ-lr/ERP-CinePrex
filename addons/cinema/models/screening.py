from odoo import fields, models
from day_enum import DayEnum

class Screening(models.Model):
    _name = 'cinema.screening'
    _description = 'Screening'

    # association auditorium <-> movie
    auditorium_id = fields.Many2one('cinema.auditorium', string='Auditorium')
    movie_id = fields.Many2one('cinema.movie', string='Movie')

    day = fields.Selection(DayEnum.DAY, string='Day of the Week')
    time = fields.Time(string='Time')
