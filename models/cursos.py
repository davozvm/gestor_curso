from odoo import models, fields


class GestorCurso(models.Model):
    _name ='gestor.curso'
    _description ='Cursos'
    
    name= fields.Char(string ='Nombre del curso', required= True)
    description= fields.Text(string= 'Descripción')
    responsable_id= fields.Many2one('res.users', string= 'Responsable', required= True)
    
    sesion_id= fields.One2many('gestor.sesion', 'course_id', string= 'Sesiones')