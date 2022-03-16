# -*- coding: utf-8 -*-

from ast import For
from odoo import models, fields, api, _

class CafeCofee(models.Model):
    _name = 'cafe.cofee'
    _description = 'Tipe of cofee'

    name = fields.Char(String='CofeeName',required = True)
    ingredientList = fields.Many2many('cafe.ingredient','cofee_ingredient_rel','cofee_id','ingredient_id',string ='Ingredients')
    cofeeAval = fields.Char(string = 'Is cofee avaliable', compute='_compute_cofeeAval')

    #Funcion del campo calculado
    def _compute_cofeeAval(self):

        for cafe in self:
            amount = 0
            for ingre in cafe.ingredientList:
                
                if(ingre.expired == 'Expired'):
                    amount +=1
                if(ingre.ingredientStock == 0):
                    amount +=1
                
            if amount == 0 :
                cafe.cofeeAval = 'Avaliable'
            else:
                cafe.cofeeAval = 'No Avaliable'
 
               


