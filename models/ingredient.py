# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class CafeIngredient(models.Model):
    _name = 'cafe.ingredient'
    
    _description = 'Ingredients of cofees'

    name = fields.Char(String='IngredientName',required = True)
    ingredientStock = fields.Float(String='IngredientStock',default = 0)
    ingredientExpiration = fields.Date(String='ExpirationDate',required = True)
    expired = fields.Char(compute="expiration")

    @api.depends("ingredientExpiration")
    def expiration(self):
        x = date.today()
        for CafeIngredient in self:
            if CafeIngredient.ingredientExpiration < x:
                CafeIngredient.expired = 'Expired'
            else:
                CafeIngredient.expired = 'Fresh'