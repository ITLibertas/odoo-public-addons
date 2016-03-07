Requirements to use KLADR widgets in XML
========================================
* Wrap the addresses in div with name kladr_address
* Replace the standard field state by the field state_id_kladr (type char)
* Add widgets to all essential fields: kladr_city, kladr_district, kladr_region, kladr_house, kladr_zip

Example
-------
Taken from [crm_kladr](https://apps.odoo.com/apps/modules/8.0/kladr_crm/ "CRM Kladr") app: 
`<div name="kladr_address"> 
<field name="country_id" placeholder="Country" class="oe_no_button" options='{"no_open": True}'/> 
<field name="city" widget="kladr_city" placeholder="City/Town" /> 
<div class="address_format"> 
            <field name="district" widget="kladr_district" placeholder="District" style="width: 50%%" /> 
            <field name="state_id" invisible="True"/>
            <field name="state_id_kladr" widget="kladr_region" placeholder="State" style="width: 50%%" on_change="onchange_state(state_id_kladr)"/>
</div>
<field name="street" placeholder="Street..." widget="kladr_street" />
<div class="address_format_house_office">
            <field name="house" placeholder="House" widget="kladr_house" style="width: 37%%" />
            <field name="office" placeholder="Office/Appartment" style="width: 39%%" />
            <field name="zip" placeholder="ZIP" widget="kladr_zip" style="width: 17%%" />
</div>`