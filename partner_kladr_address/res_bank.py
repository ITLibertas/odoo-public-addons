# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
class res_partner_bank(osv.osv):
    _inherit = "res.partner.bank"
    _columns ={
        'name': fields.char('Bank Account',size=256),
        'bank_name':fields.char('Bank Name', size=256),
    }    
    def onchange_partner_id(self, cr, uid, id, partner_id, context=None):
        result = {}
        if partner_id:
            part = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            result['owner_name'] = part.name
            result['street'] = part.street or False
            result['city'] = part.city or False
            result['zip'] =  part.zip or False
            result['country_id'] =  part.country_id.id
            result['state_id'] = part.state_id.name
        return {'value': result}
res_partner_bank()	


class Bank(osv.osv):
    _inherit = 'res.bank'
    _columns ={
        'name': fields.char('Bank Account',size=256),
    }
Bank()