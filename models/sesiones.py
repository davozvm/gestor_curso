from odoo import models, fields


class GestorSesion(models.Model):
    _name = 'gestor.sesion'
    _description= 'Sesión'
    
    name= fields.Char('Nombre de la sesión', required= True)
    course_id= fields.Many2one('gestor.curso', string= 'Curso', required= True, ondelete= 'cascade')
    
    start_date= fields.Date(string= 'Fecha de inicio')
    duration= fields.Float(string= 'Duración de la sesión')
    seats= fields.Integer(string= 'Lugares disponibles')
    instructor_id= fields.Many2one('res.users', string= 'Instructor', required= True)