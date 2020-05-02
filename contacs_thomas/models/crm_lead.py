# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BenefitCenter(models.Model):
    _name = 'benefit.center'

    name = fields.Char('Centro de Beneficio')

class CrmSegment(models.Model):
    _name = 'crm.segment'

    name = fields.Char('Segmento')


class BussinetsUnits(models.Model):
    _name = 'bussinets.units'

    name = fields.Char('Unidad de negocio')


class CrmCompetitor(models.Model):
    _name = 'crm.competitor'

    competitor_name = fields.Many2one('crm.competitor.competitor', string="Nombre Competidor")
    weaknesses = fields.Many2many('crm.weaknesses', string="Debilidades")
    strengths = fields.Many2many('crm.strengths', string="Fortalezas")
    competitor_ids = fields.Many2one('crm.lead')

    
class CrmCompetitorCompetitor(models.Model):
    _name = 'crm.competitor.competitor'

    name = fields.Char('nombre')


class CrmStrengths(models.Model):
    _name = 'crm.strengths'

    name = fields.Char('Fortalezas')


class CrmWeaknesses(models.Model):
    _name = 'crm.weaknesses'

    name = fields.Char('Debilidades')


class TemporaryUnion(models.Model):
    _name = 'temporary.union'

    name = fields.Many2one('temporary.union.name', 'Miembro de la unión temporal')
    participation = fields.Float('% Participación', invisible=True)
    funtions = fields.Text('Funciones', invisible=True)
    temporary_union_ids = fields.Many2one('crm.lead', invisible=True)


class TemporaryUnionName(models.Model):
    _name = 'temporary.union.name'

    name = fields.Char('Miembro de la unión temporal')


class CrmCost(models.Model):
    _name = 'crm.cost'

    name = fields.Many2one('crm.cost.name')
    cost_value = fields.Float('Valor')
    cost_realted_ids= fields.Many2one('crm.lead')

class CompanyInvoices(models.Model):
    _name = 'company.invoices'

    name = fields.Char('Empresa que factura')

class CrmCostName(models.Model):
    _name = 'crm.cost.name'

    name = fields.Char('Costo')


class UnspscCode(models.Model):
    _name = 'unspsc.code'

    name = fields.Char('Código')
    code_name = fields.Char(string='Nombre')


class CrmBugdet(models.Model):
    _inherit = 'crm.team'

    budget = fields.Float('Presupuesto', tracking=True)

class Lead2OpportunityPartnerThomas(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    
    @api.model
    def default_get(self, fields):
        """ Default get for name, opportunity_ids.
            If there is an exisitng partner link to the lead, find all existing
            opportunities links with this partner to merge all information together
        """
        result = super(Lead2OpportunityPartnerThomas, self).default_get(fields)
        result['name']='convert'
        return result
        
class CrmLead(models.Model):
    _inherit = 'crm.lead'
################################################
    partner_id = fields.Many2one(tracking=True, required=True)
    user_id = fields.Many2one(tracking=True, required=True)
    company_id = fields.Many2one(tracking=True, required=True)
    create_date = fields.Date(tracking=True, readonly=True)
###################################################
    stage_from = fields.Char(related='stage_id.name', string="Campo test")
    check_cost_table = fields.Boolean(compute='_check_cost', invisible=True)
    check_union_temporal= fields.Boolean(compute='_check_union', invisible=True)
    check_tag_ids = fields.Boolean(compute='_compute_check_tag_ids', invisible=True)
    check_stage = fields.Boolean(compute='stage_prop', invisible=True)
    customer_type_crm = fields.Selection([('PROSPECTO', 'PROSPECTO'),
                                      ('ACTUAL', 'ACTUAL'),
                                      ('INACTIVO', 'INACTIVO')], string="Tipo de cliente", compute='_get_customer_type', required=True)

    tender_status = fields.Selection([('PRE-PLIEGO', 'PRE-PLIEGO'),
                                      ('PLIEGO', 'PLIEGO'),
                                      ('SUBASTA', 'SUBASTA')], tracking=True)

    benefit_center=fields.Many2one('benefit.center', string="Centro de beneficios", tracking=True)
    segment_crm = fields.Many2one('crm.segment', string="Segmento", tracking=True)
    bussinets_units = fields.Many2one('bussinets.units', tracking=True)
    budget_from = fields.Float(compute='_get_budget', string='Presupuesto', tracking=True)
    email_from = fields.Char(required=True)
    partner_address_phone = fields.Char(required=True)
   # company_from = fields.Many2one('res.partner', string='Compañia')
    ############### Grupo Motivo de perdida ############################
    contact_personal = fields.Char('Contacto por cambio de personal')
    winner_competitor = fields.Many2one('crm.competitor.competitor', string='Competidor ganador')
    winner_price = fields.Float('Precio ganador')
    required_time = fields.Char('Tiempo requerido')
    price_offered = fields.Char('Precio ofertado por Thomas')
    lost_problem = fields.Char('Problema de calidad o motivo de perdida')
    requeriments_no_fulfill = fields.Char('Requisitos no cumplidos')
    observations = fields.Char('Observaciones')
    #lost_lead_id = fields.Many2one('crm.lead.lost')
    #contact_personal_from = fields.Char('Contacto', related='lost_lead_id.contact_personal')
    ###########################################################################
    comercial_manager_approval = fields.Selection([('SI', 'SI'),
                                                 ('NO', 'NO')], string='Aprobación Viabilidad Gerencia Comercial', tracking=True)
    executive_approval = fields.Selection([('SI', 'SI'),
                                                 ('NO', 'NO')], string='Aprobación junta directiva', tracking=True)
    date_deadline = fields.Date(required=True, tracking=True)
    #management_approval = fields.Selection([('SI', 'SI'),
     #                                 ('NO', 'NO')], string="Aprobación Viabilidad de Gerencia Comercia")
    billing_potencial = fields.Selection([('1M-10M', '1M-10M'),
                                      ('10M-20M', '10M-20M'),
                                      ('20M-50M', '20M-50M'),
                                      ('50M-100M', '50M-100M'),
                                      ('100M-500M', '100M-500M'),
                                      ('MÁS DE 500M', 'MÁS DE 500M')], string="Potencial de Facturación", required='True' )
    tender_type = fields.Selection([('PÚBLICA', 'PÚBLICA'),
                                      ('MÍNIMA CUANTÍA', 'MÍNIMA CUANTÍA'),
                                      ('DIRECTA', 'DIRECTA'),
                                      ('PRIVADA', 'PRIVADA'),
                                      ('SUBASTA', 'SUBASTA')], string="Tipo de Licitación")
    web_page_tender = fields.Char('Página Web licitación')
    process_number = fields.Char('Número de proceso', tracking=True)
    object_crm = fields.Char('Objeto', tracking=True)
    tender_budget = fields.Float('Prespuesto de licitación', tracking=True)
    opening_date = fields.Date('Fecha de apertura de licitación', tracking=True)
    close_date = fields.Date('Fecha de cierre de licitación', tracking=True)
    #####################COMPETIDORES##################################
    competitor = fields.One2many('crm.competitor', 'competitor_ids', string='Competidores', tracking=True)
    #########################UNION TEMPORAL ################################################
    temporary_union = fields.Selection([('SI', 'SI'),
                                      ('NO', 'NO')], string="¿ Requiere Unión Temporal ?", tracking=True)
    name_union = fields.Char('Nombre unión temporal', tracking=True)
    initials_union = fields.Char('Sigla unión temporal', tracking=True)
    temporary_union_id = fields.Many2one('temporary.union', tracking=True)
    leader_union_name = fields.Many2one('temporary.union.name', tracking=True)
   # leader_union_name_name = fields.Char(related='leader_union_id.name.name', string="Test Lider")
    company_invoices_id = fields.Many2one('temporary.union.name', 'Empresa que factura', tracking=True)
    member_union_id = fields.One2many('temporary.union', 'temporary_union_ids')
    cost_id = fields.One2many('crm.cost', 'cost_realted_ids', tracking=True)
    cost_total = fields.Float('Costo Total', tracking=True)
    quantity = fields.Float('Cantidad', tracking=True)
    unit_price = fields.Float('Precio Unitario', tracking=True)
    price_n_iva = fields.Float('Precio total sin IVA', tracking=True)
    contribution_percentage = fields.Float('Porcentaje de contribución', tracking=True)
    ###########################################################################
    opportuny_situation = fields.Text('Situación de la oportunidad', required='True')
    ###########################################################################
    comercial_approval = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Aprobación Gerencia Comercial', tracking=True)
    financial_approval = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Aprobación Gerencia Financiera ', tracking=True)
    type_contract = fields.Selection([('CONTRATO', 'CONTRATO'),
                                      ('ORDEN DE COMPRA', 'ORDEN DE COMPRA'),
                                      ('APROBACIÓN PROPUESTA', 'APROBACIÓN PROPUESTA')], string='Tipo de Contrato', tracking=True)
    contract_number = fields.Char('Número de Contrato', tracking=True)
    subscription_date = fields.Date('Fecha de suscripción', tracking=True)
    subscription_start = fields.Date('Fecha de inicio', tracking=True)
    subscription_end = fields.Date('Fecha de terminación', tracking=True)
    approval_director = fields.Boolean('Aprobación de director comercial', tracking=True)
    object_contract = fields.Char('Objeto de contrato', tracking=True)
    inicial_contract_value = fields.Float('Valor inicial del contrato', tracking=True)
    executed_contract_value = fields.Float('Valor ejecutado del contrato', tracking=True)
    act_liquidation = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Acta de liquidación', tracking=True)
    liquidation_date = fields.Date('Fecha del acta de liquidación', tracking=True)
    ####################################################################################################
    code_id = fields.Many2many('unspsc.code')
    tag_ids = fields.Many2many('crm.lead.tag', 'crm_lead_tag_rel', 'lead_id', 'tag_id', string='Tags', help="Classify and analyze your lead/opportunity categories like: Training, Service", tracking=True, required=True)
    observations_contract=fields.Char('Observaciones')

    @api.depends('partner_id')
    def _get_customer_type(self):
        for line in self:
            line.customer_type_crm = line.partner_id.customer_type

    @api.depends('team_id')
    def _get_budget(self):
        for line in self:
            line.budget_from = line.team_id.budget

    @api.onchange('date_deadline')
    def _onchange_company_id(self):
        if self.company_id:
            self.company_from = self.company_id

    ###Forzar una seleccion de un many2many
    @api.onchange('tag_ids')
    def force_one_selection(self):
        if self.tag_ids and len(self.tag_ids) > 1:
                self.tag_ids = [(6, 0, self.employee_ids[0].id)]

    ###Verificar si categoria lic es seleccionado al hacer cambios
    @api.depends('tag_ids')
    def _compute_check_tag_ids(self):
        for record in self:
            record.check_tag_ids = True if record.tag_ids and record.tag_ids[0].name == 'LICITACIÓN' else False

    ###Verificar si el estado esta en propuesta de oportunidad
    @api.depends('stage_id')
    def stage_prop(self):
        for record in self:
            record.check_stage = True if record.type == 'opportunity' and record.stage_id.id == 3 else False

    #####################################################VERIFICANDO REGISTRO EN TABLA DE UNION TEMPORAL
    @api.onchange('check_union_temporal','temporary_union','member_union_id')
    def _check_union(self):
        for record in self:
            if record.temporary_union == 'SI' and not record.member_union_id.name.name and not record.member_union_id.participation and not record.member_union_id.funtions:
                record.check_union_temporal = True 
            else:
                record.check_union_temporal = False

    @api.constrains('check_union_temporal', 'member_union_id', 'temporary_union')
    def _check_error_union(self):
            for record in self:
                if record.check_union_temporal == True:
                    raise ValidationError("Es necesario registrar datos en la tabla de Union temporal")
    #####################################################VERIFICANDO REGISTRO EN TABLA DE COSTOS
    @api.onchange('cost_id','stage_id')
    def _check_cost(self):
        for record in self:
            if record.check_stage == True and not record.cost_id.name and not record.cost_id.cost_value:
                record.check_cost_table = True 
            else:
                record.check_cost_table = False

   ###################################Verificar que la tabla de costos esté llena para poder cambiar de estado ################
    def write(self, values):
        #####
        if values.get('stage_id') and self.stage_id.id == 3 and self.type == 'opportunity':
            if not self.cost_id and not values.get('cost_id'):
                raise ValidationError("Es necesario registrar la tabla de Costos cuando el estado se encuentra en Propuesta")
        res = super(CrmLead, self).write(values)
        if self.stage_id.id != 3 and not self.cost_id and self.type == 'Es necesario registrar la tabla de Costos cuando el estado se encuentra en Propuesta':
            raise ValidationError("Es necesario registrar la tabla de Costos cuando el estado se encuentra en Propuesta")
        return res
    ##########################################################################################
    def get_table_competition(self):
        '''
        <table>
            <tr>
                <th>Nombre</th>
            </tr>
            <tr>
                <td>Nombre 1</td>
            </tr>
            <tr>
                <td>Nombre 2</td>
            </tr>
        </table> 
        '''
        table = ''
        table += ''' 
            <table>
                <tr>
                    <th>Competidor</th>
                </tr>
        '''
        flag = False
        for competitor in self.competitor:
            flag = True
            table += '<tr> <td>' + competitor.competitor_name.name + '</td> </tr>'
        
        table += ''' 
            </table> 
        '''
        return table if flag else False

    def get_table_member(self):
        '''
        <table>
            <tr>
                <th>Nombre</th>
            </tr>
            <tr>
                <td>Nombre 1</td>
            </tr>
            <tr>
                <td>Nombre 2</td>
            </tr>
        </table> 
        '''
        table = ''
        table += ''' 
            <table>
                <tr>
                    <th>Nombre</th>
                    <th>Participacion</th>
                    <th>Funcion</th>
                </tr>
        '''
        flag = False
        for  member_union_id in self.member_union_id:
            flag = True
            table += '<tr>'
            table += '<td>' + member_union_id.name.name + '  </td>'
            table += '<td>' + str(member_union_id.participation) + '  </td>'
            table += '<td>' + member_union_id.funtions + '  </td>'
            table += '</tr>'
        table += ''' 
            </table> 
        '''
        return table if flag else False
