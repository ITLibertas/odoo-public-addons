# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
class res_partner(osv.osv):
    _inherit = "res.partner"
    def z_full_r_address(self, cr, uid, ids, field_name, args, context=None):
         res = {}        
         partner_address=''
         if ids:
            partner = self.browse(cr,uid,ids[0])
            if partner:
                if partner.zip:
                    partner_address = partner.zip
                if partner.state_id_kladr:
                    if partner_address != '':
                        if partner.state_id_kladr:
                            partner_address = partner_address + ', '+partner.state_id_kladr
                    else:
                        if partner.state_id_kladr:
                            partner_address = partner.state_id_kladr
                if partner.district:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.district
                    else:
                        partner_address = partner.district          
                if partner.city:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.city
                    else:
                        partner_address = partner.city
                if partner.street:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.street
                    else:
                        partner_address = partner.street            
                if partner.house:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.house
                    else:
                        partner_address =  partner.house    
                if partner.office:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.office
                    else:
                        partner_address =  partner.office
         for obj in self.browse(cr, uid, ids, context=context):
            res[obj.id] = partner_address
         return res
    def z_full_real_address(self, cr, uid, ids, field_name, args, context=None):
         res = {}
         partner_address=''
         if ids:
            partner = self.browse(cr,uid,ids[0])
            if partner:
                if partner.zip_real:
                    partner_address = partner.zip_real
                if partner.state_id_real:
                    if partner_address != '':
                        if partner.state_id_real:
                            partner_address = partner_address + ', '+partner.state_id_real
                    else:
                        if partner.state_id_real:
                            partner_address = partner.state_id_real
                if partner.district_real:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.district_real
                    else:
                        partner_address = partner.district_real          
                if partner.city_real:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.city_real
                    else:
                        partner_address = partner.city_real
                if partner.street_real:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.street_real
                    else:
                        partner_address = partner.street_real            
                if partner.house_real:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.house_real
                    else:
                        partner_address =  partner.house_real    
                if partner.office_real:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.office_real
                    else:
                        partner_address =  partner.office_real
         for obj in self.browse(cr, uid, ids, context=context):
            res[obj.id] = partner_address         
         return res
    def z_full_post_address(self, cr, uid, ids, field_name, args, context=None):
         res = {}
         partner_address=''
         if ids:
            partner = self.browse(cr,uid,ids[0])
            if partner:
                if partner.zip_post:
                    partner_address = partner.zip_post
                if partner.state_id_post:
                    if partner_address != '':
                        if partner.state_id_post:
                            partner_address = partner_address + ', '+partner.state_id_post
                    else:
                        if partner.state_id_post:
                            partner_address = partner.state_id_post
                if partner.district_post:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.district_post
                    else:
                        partner_address = partner.district_post          
                if partner.city_post:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.city_post
                    else:
                        partner_address = partner.city_post
                if partner.street_post:
                    if partner_address != '':
                        partner_address = partner_address + ', '+partner.street_post
                    else:
                        partner_address = partner.street_post            
                if partner.house_post:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.house_post
                    else:
                        partner_address =  partner.house_post    
                if partner.office_post:
                    if partner_address != '':
                        partner_address = partner_address + ', '+ partner.office_post
                    else:
                        partner_address =  partner.office_post 
         for obj in self.browse(cr, uid, ids, context=context):
            res[obj.id] = partner_address         
         return res
    def onchange_state(self, cr, uid, id, state_name, context=None):
        result = {}
        state_ids = self.pool.get('res.country.state').search(cr,uid,[('name', '=', state_name)],context=None)
        if state_ids:
            state_obj = self.pool.get('res.country.state').browse(cr, uid, state_ids, context=context)
            if state_ids:
                result['state_id'] = state_obj[0].id
        return {'value': result}

    _columns = {
        'district': fields.char('District', size=128),
        'state_id_kladr': fields.char('State', size=128),
        'house': fields.char('House', size=64),
        'office': fields.char('Office', size=64),
        'full_r_address':fields.function(z_full_r_address,string="Full address", type="char"),
        #Real address
        'country_id_real': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'city_real': fields.char('City', size=128),
        'street_real': fields.char('Street', size=128),
        'zip_real': fields.char('Zip', change_default=True, size=24),
        'district_real': fields.char('District', size=128),
        'state_id_real': fields.char('State', size=128),
        'house_real': fields.char('House', size=64),
        'office_real': fields.char('Office', size=64),
        'full_real_address':fields.function(z_full_real_address,string="Full address", type="char"),
        #Post address
        'country_id_post': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'city_post': fields.char('City', size=128),
        'street_post': fields.char('Street', size=128),
        'zip_post': fields.char('Zip', change_default=True, size=24),
        'district_post': fields.char('District', size=128),
        'state_id_post': fields.char('State', size=128),
        'house_post': fields.char('House', size=64),
        'office_post': fields.char('Office', size=64), 
        'full_post_address':fields.function(z_full_post_address,string="Full address", type="char"),             
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
