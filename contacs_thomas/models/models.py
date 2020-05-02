# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AdressContact(models.Model):
    _name = 'adress.contact'

    name = fields.Char('Model: adress')

class StreetCode(models.Model):
    _name = 'street.code'

    name = fields.Char('Descripción')
    code = fields.Char('Código')
    company_id = fields.Many2one('res.company')

class AdressCode(models.Model):
    _name = 'address.code'

    name = fields.Char('Descripción')
    code = fields.Char('Código')
    company_id = fields.Many2one('res.company')

class CiiuValue(models.Model):
    _name = 'ciiu.value'

    name = fields.Char('Descripción')
    code = fields.Char('Código')
    company_id = fields.Many2one('res.company')

class ResIndicativeState(models.Model):
    _inherit = 'res.country.state'

    indicative_state_code = fields.Integer(string="Indicativo de provincia")

class ResPartner(models.Model):
    _inherit = 'res.partner'

   # company_type = fields.Selection(string='Company Type',
    #    selection=[('person', 'Individual'), ('company', 'Company')],
     #   compute='_compute_company_type', inverse='_write_company_type', required='True')
     ################## GRUPO NOMBRE DE CLIENTE Y COMPAÑIA #####################3
    firts_name = fields.Char('Nombre 1')
    last_name = fields.Char('Nombre 2')
    middle_name = fields.Char('Nombre 3')
    second_last_name = fields.Char('Nombre 4')
    company_name=fields.Char('Nombre de la compañía')
    company_nature = fields.Selection([('S.A.S', 'S.A.S'),
                                      ('S.A', 'S.A'),
                                      ('LTDA', 'LTDA'),
                                      ('PERSONA NATURAL', 'PERSONA NATURAL'),
                                      ('EMPRESA UNIPERSONAL', 'EMPRESA UNIPERSONAL'),
                                      ('SOCIEDAD COLECTIVA', 'SOCIEDAD COLECTIVA'),
                                      ('S. EN C.', 'S. EN C.'),
                                      ('S.C.A', 'S.C.A')], string="Naturaleza de la compañía")
    field_1 = fields.Many2one('address.code')
    field_2  = fields.Integer('Campo direccion 2')
    field_3 = fields.Selection([('A', 'A'),
                                      ('B', 'B'),
                                      ('C', 'C'),
                                      ('D', 'D'),
                                      ('E', 'E'),
                                      ('F', 'F'),
                                      ('G', 'G'),
                                      ('H', 'H'),
                                      ('I', 'I'),
                                      ('J', 'J'),
                                      ('K', 'K'),
                                      ('L', 'L'),
                                      ('M', 'M'),
                                      ('N', 'N'),
                                      ('Ñ', 'Ñ'),
                                      ('O', 'O'),
                                      ('P', 'P'),
                                      ('Q', 'Q'),
                                      ('R', 'R'),
                                      ('S', 'S'),
                                      ('T', 'T'),
                                      ('U', 'U'),
                                      ('V', 'V'),
                                      ('W', 'W'),
                                      ('X', 'X'),
                                      ('Y', 'Y'),
                                      ('Z', 'Z'),
                                      ], string="Campo dirección 3")
    field_4 = fields.Many2one('street.code')
    field_5  = fields.Integer('Campo direccion 5')
    field_6 = fields.Selection([('A', 'A'),
                                      ('B', 'B'),
                                      ('C', 'C'),
                                      ('D', 'D'),
                                      ('E', 'E'),
                                      ('F', 'F'),
                                      ('G', 'G'),
                                      ('H', 'H'),
                                      ('I', 'I'),
                                      ('J', 'J'),
                                      ('K', 'K'),
                                      ('L', 'L'),
                                      ('M', 'M'),
                                      ('N', 'N'),
                                      ('Ñ', 'Ñ'),
                                      ('O', 'O'),
                                      ('P', 'P'),
                                      ('Q', 'Q'),
                                      ('R', 'R'),
                                      ('S', 'S'),
                                      ('T', 'T'),
                                      ('U', 'U'),
                                      ('V', 'V'),
                                      ('W', 'W'),
                                      ('X', 'X'),
                                      ('Y', 'Y'),
                                      ('Z', 'Z'),
                                      ], string="Campo dirección 6")
    field_7 = fields.Many2one('street.code')
    field_8  = fields.Integer('Campo direccion 8')
    field_9 = fields.Many2one('address.code')
    field_10  = fields.Integer('Campo direccion 10')
    field_11 = fields.Many2one('address.code')
    field_12  = fields.Integer('Campo direccion 12')
    ################################################################################
    l10n_co_document_type = fields.Selection([('rut', 'NIT'),
                                              ('id_document', 'Cédula'),
                                              ('id_card', 'Tarjeta de Identidad'),
                                              ('passport', 'Pasaporte'),
                                              ('foreign_id_card', 'Cédula Extranjera'),
                                              ('external_id', 'ID del Exterior'),
                                              ('diplomatic_card', 'Carné Diplomatico'),
                                              ('residence_document', 'Salvoconducto de Permanencia'),
                                              ('civil_registration', 'Registro Civil'),
                                              ('national_citizen_id', 'Cédula de ciudadanía')], string='Document Type',
                                             help='Indicates to what document the information in here belongs to.')
    nit  = fields.Char('NIT')
    dv = fields.Selection([('0', '0'),
                                      ('1', '1'),
                                      ('2', '2'),
                                      ('3', '3'),
                                      ('4', '4'),
                                      ('5', '5'),
                                      ('6', '6'),
                                      ('7', '7'),
                                      ('8', '8'),
                                      ('9', '9')
                                      ], string="DV")
    ciiu = fields.Many2many('ciiu.value', string="CIIU")
    rut  = fields.Binary('RUT')
    main_road = fields.Many2one('adress.contact', string="Vía principal")
    main_road_name=fields.Char('Nombre vía principal', placeholder='38A BIS')
    generating_route = fields.Char('Vía generadora:', placeholder='20B')
    farm = fields.Char('Predio', required='True', placeholder='61')
    complement_adress = fields.Char('Complemento', placeholder='SUR')
    full_adress = fields.Char('Dirección Completa')
    res_lang_id = fields.Many2one('res.lang', string="Idioma")
    indicative_state = fields.Integer('Indicativo Provincia', compute='_get_indicative_state')
    indicative_country = fields.Integer('Indicativo País', related='country_id.phone_code')
    consult_order = fields.Selection([('REPORTADO', 'REPORTADO'),
                                      ('NO REPORTADO', 'NO REPORTADO')], string="Consulta lista restrictiva")

    consult_date = fields.Date('Fecha de consulta', tracking=True)

    approval_compliance = fields.Selection([('SI', 'SI'),
                                            ('NO', 'NO'),
                                            ('NO APLICA', 'NO APLICA')], string="Aproción Oficial de cumplimiento")

    risk_profile= fields.Char('Perfil de riesgo')
    risk_percentage = fields.Float('Porcentaje de riesgo')

    customer_type = fields.Selection([('PROSPECTO', 'PROSPECTO'),
                                      ('ACTUAL', 'ACTUAL'),
                                      ('INACTIVO', 'INACTIVO')], string="Tipo de cliente")
    departure_date = fields.Date('Fecha de salida')
    sector = fields.Selection([('PÚBLICO', 'PÚBLICO'),
                                      ('PRIVADO', 'PRIVADO'),
                                      ('MIXTO', 'MIXTO')], string="Sector")
    date_update = fields.Date('Fecha de Actualización de datos')
    billing_potencial = fields.Selection([('1M-10M', '1M-10M'),
                                      ('10M-20M', '10M-20M'),
                                      ('20M-50M', '20M-50M'),
                                      ('50M-100M', '50M-100M'),
                                      ('100M-500M', '100M-500M'),
                                      ('Más de 500M', 'Más de 500M')], string="Potencial de Facturación")

    rol = fields.Selection([('user', 'USUARIO'),
                           ('evaluate', 'EVALUA'),
                           ('influence', 'INFLUENCIA'),
                           ('decides', 'DECIDE'),
                           ('approves', 'APRUEBA')], string="Rol")
    attitude = fields.Selection([('PADRINO', 'PADRINO'),
                           ('AMIGO', 'AMIGO'),
                           ('NEUTRAL', 'NEUTRAL'),
                           ('OPOSITOR', 'OPOSITOR'),
                           ('ENEMIGO', 'ENEMIGO')], string="Actitud")

    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

  # concatenar nombre completo del empleado o nombre de la empresa
    @api.onchange('company_type','company_name','company_nature','first_name', 'last_name', 'middle_name', 'second_last_name')
    def _onchange_nombre_completo(self):
            if  self.company_type=='person':
                self.name = "%s %s %s %s" % (
                self.firts_name if self.firts_name else "",
                self.last_name if self.last_name else "",      
                self.middle_name if self.middle_name else "",        
                self.second_last_name if self.second_last_name else "")
            else:
                self.name = "%s %s" % (
                self.company_name if self.company_name else "",
                self.company_nature if self.company_nature else "")

    # concatenar dirección completa
    @api.onchange('field_1','field_2','field_3','field_4', 'field_5', 'field_6', 'field_7', 
                  'field_8', 'field_9', 'field_10', 'field_11', 'field_12')
    def _onchange_full_address(self):
                self.street = "%s %s %s %s %s %s %s %s %s %s %s %s" % (
                self.field_1.code if self.field_1.code else "",
                self.field_2 if self.field_2 else "",      
                self.field_3 if self.field_3 else "",        
                self.field_4.name if self.field_4.name else "",
                self.field_5 if self.field_4 else "",
                self.field_6 if self.field_6 else "",
                self.field_7.name if self.field_7.name else "",
                self.field_8 if self.field_8 else "",
                self.field_9.code if self.field_9.code else "",
                self.field_10 if self.field_10 else "",
                self.field_11.code if self.field_11.code else "",
                self.field_12 if self.field_12 else "")


    ##### Agregar archivo rut a adjuntos
    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        if 'rut' in vals:
            dic = {
                'name': 'rut',
                'datas': vals['rut'],
                'res_model': 'res.partner',
                'res_id': res.id
            }
            self.env['ir.attachment'].create(dic)

        return res
    
    def write(self, vals):
        res = super(ResPartner, self).write(vals)
        for record in self:
            if 'rut' in vals:
                dic = {
                    'name': 'rut',
                    'datas': vals['rut'],
                    'res_model': 'res.partner',
                    'res_id': record.id
                }
                self.env['ir.attachment'].create(dic)
            
        return res

    @api.depends('state_id')
    def _get_indicative_state(self):
        for line in self:
            line.indicative_state = line.state_id.indicative_state_code

    @api.constrains('company_type', 'child_ids')
    def _check_child(self):
        for record in self:
            if record.company_type == 'company' and not record.child_ids:
                raise ValidationError("Es necesario registrar por lo menos un contactos en esta compañía")

    @api.depends('company_name')
    def _get_customer_name(self):
        for line in self:
            line.name = line.company_name

class BenefitCenter(models.Model):
    _name = 'benefit.center'

    name = fields.Char('Centro de Beneficio')
    segment_crm = fields.Many2one('crm.segment', string="Segmento")
    bussinets_units = fields.Many2one('bussinets.units', string="Unidad de negocio")

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
    participation = fields.Float('% Participación')
    funtions = fields.Text('Funciones')
    temporary_union_ids = fields.Many2one('crm.lead')
class TemporaryUnionName(models.Model):
    _name = 'temporary.union.name'

    name = fields.Char('Miembro de la unión temporal')

class CrmCost(models.Model):
    _name = 'crm.cost'

    name = fields.Many2one('crm.cost.name')
    cost_value = fields.Float('Valor')
    cost_realted_ids= fields.Many2one('crm.lead')

class CrmCostName(models.Model):
    _name = 'crm.cost.name'

    name = fields.Char('Costo')

class UnspscCode(models.Model):
    _name = 'unspsc.code'

    name = fields.Char('Código')
    code_name = fields.Char(string='Nombre')

class CrmBugdet(models.Model):
    _inherit = 'crm.team'

    budget = fields.Float('Presupuesto')

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

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    #name = fields.Many2one('res.currency', 'Currency')
    stage_from = fields.Char(related='stage_id.name', string="Campo test")
    test_stage_ids = fields.Boolean(string="Test boleano", compute='_get_category')
    customer_type_crm = fields.Selection([('PROSPECTO', 'PROSPECTO'),
                                      ('ACTUAL', 'ACTUAL'),
                                      ('INACTIVO', 'INACTIVO')], string="Tipo de cliente", compute='_get_customer_type')

    tender_status = fields.Selection([('PRE-PLIEGO', 'PRE-PLIEGO'),
                                      ('PLIEGO', 'PLIEGO'),
                                      ('SUBASTA', 'SUBASTA')], string="Estado de licitación")

    benefit_center=fields.Many2one('benefit.center', string="Centro de beneficios")
    segment_crm_from = fields.Char(related='benefit_center.segment_crm.name')
    bussinets_units_from = fields.Char(related='benefit_center.bussinets_units.name')
    budget_from = fields.Float(compute='_get_budget', string='Presupuesto', required=True)
   # company_from = fields.Many2one('res.partner', string='Compañia')
    ############### Grupo Motivo de perdida ############################
    #lost_lead_id = fields.Many2one('crm.lead.lost')
    #contact_personal_from = fields.Char('Contacto', related='lost_lead_id.contact_personal')
    ###########################################################################
    comercial_manager_approval = fields.Selection([('SI', 'SI'),
                                                 ('NO', 'NO')], string='Aprobación Viabilidad Gerencia Comercial')
    executive_approval = fields.Selection([('SI', 'SI'),
                                                 ('NO', 'NO')], string='Aprobación junta directiva')
    #create_date_from=fields.Datetime('Creado', compute='_get_date_deadline', required='True')
    #management_approval = fields.Selection([('SI', 'SI'),
     #                                 ('NO', 'NO')], string="Aprobación Viabilidad de Gerencia Comercia")
    billing_potencial = fields.Selection([('1M-10M', '1M-10M'),
                                      ('10M-20M', '10M-20M'),
                                      ('20M-50M', '20M-50M'),
                                      ('50M-100M', '50M-100M'),
                                      ('100M-500M', '100M-500M'),
                                      ('Más de 500M', 'Más de 500M')], string="Potencial de Facturación")
    tender_type = fields.Selection([('PÚBLICA', 'PÚBLICA'),
                                      ('MÍNIMA', 'MÍNIMA'),
                                      ('CUÁNTICA', 'CUÁNTICA'),
                                      ('DIRECTA', 'DIRECTA'),
                                      ('PRIVADA', 'PRIVADA'),
                                      ('SUBASTA', 'SUBASTA')], string="Tipo de Licitación")
    web_page_tender = fields.Char('Página Web licitación')
    process_number = fields.Char('Número de proceso')
    object_crm = fields.Char('Objeto')
    tender_budget = fields.Float('Prespuesto de licitación')
    opening_date = fields.Date('Fecha de apertura de licitación')
    close_date = fields.Date('Fecha de cierre de licitación')
    competitor = fields.One2many('crm.competitor', 'competitor_ids', string='Competidores')
    temporary_union = fields.Selection([('SI', 'SI'),
                                      ('NO', 'NO')], string="¿ Requiere Unión Temporal ?")
    name_union = fields.Char('Nombre unión temporal')
    initials_union = fields.Char('Sigla unión temporal')
    leader_union_id = fields.Many2one('temporary.union', 'Lider unión temporal')
    company_invoices_id = fields.Char('Empresa que factura')
    member_union_id = fields.One2many('temporary.union', 'temporary_union_ids')
    cost_id = fields.One2many('crm.cost', 'cost_realted_ids')
    cost_total = fields.Float('Costo Total')
    quantity = fields.Float('Cantidad')
    unit_price = fields.Float('Precio Unitario')
    price_n_iva = fields.Float('Precio total sin IVA')
    contribution_percentage = fields.Float('Porcentaje de contribución')
    ###########################################################################
    opportuny_situation = fields.Text('Situación de la oportunidad')
    ###########################################################################
    comercial_approval = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Aprobación Gerencia Comercial')
    financial_approval = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Aprobación Gerencia Financiera ')
    type_contract = fields.Selection([('CONTRATO', 'CONTRATO'),
                                      ('ORDEN DE COMPRA', 'ORDEN DE COMPRA'),
                                      ('APROBACIÓN PROPUESTA', 'APROBACIÓN PROPUESTA')], string='Tipo de Contrato')
    contract_number = fields.Char('Número de Contrato')
    subscription_date = fields.Date('Fecha de suscripción')
    subscription_start = fields.Date('Fecha de inicio')
    subscription_end = fields.Date('Fecha de terminación')
    approval_director = fields.Boolean('Aprobación de director comercial')
    object_contract = fields.Char('Objeto de contrato')
    inicial_contract_value = fields.Float('Valor inicial del contrato')
    executed_contract_value = fields.Float('Valor ejecutado del contrato')
    act_liquidation = fields.Selection([('SI', 'SI'),
                                           ('NO', 'NO')], string='Acta de liquidación')
    liquidation_date = fields.Date('Fecha del acta de liquidación')
    code_id = fields.Many2many('unspsc.code')
    tag_ids = fields.Many2many('crm.lead.tag', 'crm_lead_tag_rel', 'lead_id', 'tag_id', string='Tags', help="Classify and analyze your lead/opportunity categories like: Training, Service")

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
            self.tag_ids = [(6, 0, self.tag_ids[1].id)]
    ###Verificar si categoria lic es seleccionado al hacer cambios
    @api.onchange('test_stage_ids','tag_ids')
    def category_selection(self):
        for record in self:
            if record.tag_ids.name == 'LICITACIÓN':
                record.test_stage_ids = True
            else:
                record.test_stage_ids = False
    #####Verificar la categoria inicial#########    
    @api.depends('tag_ids','test_stage_ids')
    def _get_category(self):
        for line in self:
            if line.tag_ids.name == 'LICITACIÓN':
                line.test_stage_ids = True
            else:
                line.test_stage_ids = False
    #####################################################
   # @api.onchange('contact_personal_from','contact_personal')
   # def _onchange_contact_personal(self):
    #    for line in self:
     #       if line.lost_reason_id:
      #          line.company_from = self.env['crm.lead.lost'].contact_personal