from odoo import fields, models

class Movie(models.Model):
    _name = 'cinema.movie'
    _description = 'A Movie'

    name = fields.Char(required=True)
    duration = fields.Integer(required=True)
    category = fields.Selection(
        string='Category',
        selection=[
            ('action', 'Action'),
            ('comedy', 'Comedy'),
            ('horror', 'Horror')
        ],
        required=True
    )