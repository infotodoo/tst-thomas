# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLeadLostThomas(models.TransientModel):
    _inherit = 'crm.lead.lost'

    contact_personal = fields.Char('Contacto por cambio de personal')
    winner_competitor = fields.Many2one('crm.competitor.competitor', string='Competidor ganador')
    winner_price = fields.Float('Precio ganador')
    required_time = fields.Char('Tiempo requerido')
    price_offered = fields.Char('Precio ofertado por Thomas')
    lost_problem = fields.Char('Problema de calidad o motivo de perdida')
    requeriments_no_fulfill = fields.Char('Requisitos no cumplidos')
    observations = fields.Char('Observaciones')

    '''def action_lost_reason_apply(self):
        # leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        # return leads.action_set_lost(lost_reason=self.lost_reason_id.id)
        res = super(CrmLeadLostThomas, self).action_lost_reason_apply()
        return res'''

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        return leads.action_set_lost(lost_reason=self.lost_reason_id.id,contact_personal=self.contact_personal,winner_competitor=self.winner_competitor.id,
                                     winner_price=self.winner_price,required_time=self.required_time,
                                     price_offered=self.price_offered,lost_problem=self.lost_problem,
                                     requeriments_no_fulfill=self.requeriments_no_fulfill,observations=self.observations)
