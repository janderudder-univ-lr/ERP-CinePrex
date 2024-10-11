from odoo import fields, models
from . import day_enum

class Screening(models.Model):
    _name = 'cinema.screening'
    _description = 'Screening'

    # association: Auditorium <-> Movie
    #                          |
    #                      Screening
    auditorium_id = fields.Many2one('cinema.auditorium', string='Auditorium')
    movie_id = fields.Many2one('cinema.movie', string='Movie')

    day = fields.Selection(day_enum.DayEnum.DAY, string='Day of the Week')
    time = fields.Float(string='Time', compute="_compute_time")
