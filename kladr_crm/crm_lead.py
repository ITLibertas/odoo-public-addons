#coding: utf-8
from openerp.osv import osv, fields
from openerp.addons.base.res.res_partner import format_address
from openerp import tools
from datetime import datetime
import time

class crm_lead(format_address, osv.osv):
    _name = "crm.lead"
    _inherit = "crm.lead"
    
    def onchange_state(self, cr, uid, id, state_name, context=None):
        result = {}
        state_ids = self.pool.get('res.country.state').search(cr,uid,[('name', '=', state_name)],context=None)
        if state_ids:
            state_obj = self.pool.get('res.country.state').browse(cr, uid, state_ids, context=context)
            if state_ids:
                result['state_id'] = state_obj[0].id
        return {'value': result}
        
    def _lead_create_contact(self, cr, uid, lead, name, is_company, parent_id=False, context=None):
        partner = self.pool.get('res.partner')
        vals = {'name': name,
            'user_id': lead.user_id.id,
            'comment': lead.description,
            'section_id': lead.section_id.id or False,
            'parent_id': parent_id,
            'phone': lead.phone,
            'mobile': lead.mobile,
            'email': tools.email_split(lead.email_from) and tools.email_split(lead.email_from)[0] or False,
            'fax': lead.fax,
            'title': lead.title and lead.title.id or False,
            'function': lead.function,
            'street': lead.street,
            'street2': lead.street2,
            'zip': lead.zip,
            'city': lead.city,
            'country_id': lead.country_id and lead.country_id.id or False,
            'state_id': lead.state_id and lead.state_id.id or False,
            'is_company': is_company,
            'district': lead.district,
            'state_id_kladr': lead.state_id_kladr,
            'house': lead.house,
            'office': lead.office,
            'type': 'contact'
        }
        partner = partner.create(cr, uid, vals, context=context)
        return partner
        
    _columns = {
        'district': fields.char('District', size=128),
        'state_id_kladr': fields.char('State', size=128),
        'house': fields.char('House', size=64),
        'office': fields.char('Office', size=64),
        }
crm_lead()