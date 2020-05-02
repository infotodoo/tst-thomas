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
    company_type = fields.Selection(tracking=True)
    company_name = fields.Char(tracking=True)
    #####################################################3333
    firts_name = fields.Char('Nombre 1')
    last_name = fields.Char('Nombre 2')
    middle_name = fields.Char('Nombre 3')
    second_last_name = fields.Char('Nombre 4')
    company_nature = fields.Selection([('S.A.S', 'S.A.S.'),
                                      ('S.A', 'S.A.'),
                                      ('LTDA', 'LTDA.'),
                                      ('ENTIDAD PRIVADA', 'ENTIDAD PRIVADA'),
                                      ('ENTIDAD ORDEN NACIONAL', 'ENTIDAD ORDEN NACIONAL'),
                                      ('ENTIDAD ORDEN TERRITORIAL', 'ENTIDAD ORDEN TERRITORIAL'),
                                      ('ENTIDAD EXTRANJERA', 'ENTIDAD EXTRANJERA'),
                                      ('ENTIDAD SIN ÁNIMO DE LUCRO', 'ENTIDAD SIN ÁNIMO DE LUCRO'),
                                      ('EMPRESA INDUSTRIAL Y COMERCIAL DEL ESTADO', 'EMPRESA INDUSTRIAL Y COMERCIAL DEL ESTADO'),
                                      ('ORGANIZACIÓN ECONOMÍA SOLIDARIA', 'ORGANIZACIÓN ECONOMÍA SOLIDARIA'),
                                      ('SOCIEDAD EN COMANDITA POR ACCIONES', 'SOCIEDAD EN COMANDITA POR ACCIONES')], string="Naturaleza de la compañía", tracking=True)
    field_1 = fields.Many2one('address.code', tracking=True)
    field_2  = fields.Char('Campo direccion 2', tracking=True)
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
                                      ], string="Campo dirección 3", tracking=True)
    field_4 = fields.Many2one('street.code', tracking=True)
    field_5  = fields.Char('Campo direccion 5', tracking=True)
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
                                      ], string="Campo dirección 6", tracking=True)
    field_7 = fields.Many2one('street.code', tracking=True)
    field_8  = fields.Char('Campo direccion 8', tracking=True)
    field_9 = fields.Many2one('address.code', tracking=True)
    field_10  = fields.Char('Campo direccion 10', tracking=True)
    field_11 = fields.Many2one('address.code', tracking=True)
    field_12  = fields.Char('Campo direccion 12', tracking=True)
    street_thomas=fields.Char('Dirección aux')
    city_crm = fields.Many2one('res.city', string='Ciudad', domain="[('state_id', '=?', state_id)]", required=True, placeholder='Ciudad')
    city=fields.Char(invisible=True)
    ################################################################################
    vat=fields.Char(required=True, tracking=True)
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
                                             help='Indicates to what document the information in here belongs to.', required=True)
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
                                      ], string="DV", tracking=True, required=True)
    ciiu = fields.Many2many('ciiu.value', string="CIIU")
    rut  = fields.Binary('RUT', tracking=True)
    file_name = fields.Char("File Name")
    ###########################################################################
    main_road = fields.Many2one('adress.contact', string="Vía principal")
    main_road_name=fields.Char('Nombre vía principal', placeholder='38A BIS')
    generating_route = fields.Char('Vía generadora:', placeholder='20B')
    farm = fields.Char('Predio', required='True', placeholder='61')
    complement_adress = fields.Char('Complemento', placeholder='SUR')
    ##############################################################################
    full_adress = fields.Char('Dirección Completa')
    lang = fields.Selection(required=True, string='Idioma')
    res_lang_id = fields.Many2one('res.lang', invisible=True)
    indicative_state = fields.Integer('Indicativo Provincia', compute='_get_indicative_state')
    indicative_country = fields.Integer('Indicativo País', related='country_id.phone_code')
    consult_order = fields.Selection([('REPORTADO', 'REPORTADO'),
                                      ('NO REPORTADO', 'NO REPORTADO')], string="Consulta lista restrictiva", tracking=True)
    email = fields.Char(required=True)

    fecha_consulta = fields.Date(tracking=True, string='Fecha de consulta')
    approval_compliance = fields.Selection([('SI', 'SI'),
                                            ('NO', 'NO'),
                                            ('NO APLICA', 'NO APLICA')], string="Aprobación Oficial de cumplimiento", tracking=True)

    risk_profile= fields.Char('Perfil de riesgo', tracking=True)
    risk_percentage = fields.Float('Porcentaje de riesgo', tracking=True)

    customer_type = fields.Selection([('PROSPECTO', 'PROSPECTO'),
                                      ('ACTUAL', 'ACTUAL'),
                                      ('INACTIVO', 'INACTIVO')], string="Tipo de cliente", tracking=True)
    departure_date = fields.Date('Fecha de salida', tracking=True)
    sector = fields.Selection([('PÚBLICO', 'PÚBLICO'),
                                      ('PRIVADO', 'PRIVADO'),
                                      ('MIXTO', 'MIXTO')], string="Sector")
    date_update = fields.Date('Fecha de Actualización de datos', tracking=True)
    billing_potencial = fields.Selection([('1M-10M', '1M-10M'),
                                      ('10M-20M', '10M-20M'),
                                      ('20M-50M', '20M-50M'),
                                      ('50M-100M', '50M-100M'),
                                      ('100M-500M', '100M-500M'),
                                      ('MÁS DE 500M', 'MÁS DE 500M')], string="Potencial de Facturación")

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
    check_colombia=fields.Boolean('Seleccion Colombia', compute='check_colombia_id', invisible='True')

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
                  'field_8', 'field_9', 'field_10', 'field_11', 'field_12', 'country_id')
    def _onchange_full_address(self):

            if self.country_id.name == 'Colombia':
                self.street = "%s %s %s %s %s %s %s %s %s %s %s %s" % (
                self.field_1.code if self.field_1.code else "",
                self.field_2 if self.field_2 else "",      
                self.field_3 if self.field_3 else "",        
                self.field_4.name if self.field_4.name else "",
                self.field_5 if self.field_5 else "",
                self.field_6 if self.field_6 else "",
                self.field_7.name if self.field_7.name else "",
                self.field_8 if self.field_8 else "",
                self.field_9.code if self.field_9.code else "",
                self.field_10 if self.field_10 else "",
                self.field_11.code if self.field_11.code else "",
                self.field_12 if self.field_12 else "")
                self.street_thomas = self.street
            else:
                self.street=self.street

    ##### Agregar archivo rut a adjuntos
    @api.model
    def create(self, vals):
        if 'street_thomas' in vals:
            vals['street'] =vals['street_thomas']
        if not 'street_thomas' in vals and not 'street' in vals:
            vals['street'] = self.street_thomas
        res = super(ResPartner, self).create(vals)
        if 'rut' in vals and vals['file_name']:
            dic = {
                'name': vals['file_name'],
                'datas': vals['rut'],
                'res_model': 'res.partner',
                'res_id': res.id
            }
            self.env['ir.attachment'].create(dic)

        return res
    
    def write(self, vals):
        if 'street_thomas' in vals:
            vals['street'] =vals['street_thomas']
        if not 'street_thomas' in vals and not 'street' in vals:
            vals['street'] = self.street_thomas
        res = super(ResPartner, self).write(vals)
        for record in self:
            if 'rut' in vals and vals['file_name']:
                dic = {
                    'name': vals['file_name'],
                    'datas': vals['rut'],
                    'res_model': 'res.partner',
                    'res_id': record.id
                }
                self.env['ir.attachment'].create(dic)
            
        return res

    @api.depends('country_id')
    def check_colombia_id(self):
        for line in self:
            if line.country_id.name == 'Colombia':
                self.check_colombia = True
            else:
                self.check_colombia = False

    @api.depends('state_id')
    def _get_indicative_state(self):
        for line in self:
            line.indicative_state = line.state_id.indicative_state_code

    @api.constrains('company_type', 'child_ids')
    def _check_child(self):
        for record in self:
            if record.company_type == 'company' and not record.child_ids:
                raise ValidationError("Es necesario registrar por lo menos un contacto en esta compañía")

    @api.depends('company_name')
    def _get_customer_name(self):
        for line in self:
            line.name = line.company_name
