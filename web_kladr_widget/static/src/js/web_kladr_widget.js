openerp.web_kladr_widget = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    var kladr_token = '53760a0bfca9161c693e34ed';
    var kladr_key = 'ab188aca338dacfddf03fbaaaf816356944a33d0';
    instance.web.form.widgets.add('kladr_city', 'instance.web_kladr_widget.kladr_cityWidget');
    instance.web_kladr_widget.kladr_cityWidget = instance.web.form.FieldChar.extend({
        template: "kladr_city",
        start: function() {
            this._super();
        },
        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
                this.$('[name="kladr_city"]').kladr({
                    token: kladr_token,
                    key: kladr_key,
                    type: $.ui.kladrObjectType.CITY,
                    withParents: true,
                    label: function(obj, query){
                            var result = '';
                            for(var i in obj.parents){
                                result += obj.parents[i].typeShort + '. ' + obj.parents[i].name + ', ';
                            }
                            result += obj.typeShort + '. ' + obj.name;
                            return result;
                        },
                    select: function( event, ui ){
                                var obj = ui.item.obj;
                                var all_div = $(this).closest('div[name="kladr_address"]')[0];
                                ui.item.value = obj.typeShort + '. ' + ui.item.value;
                                $(all_div).find('input[name="kladr_region"]').val('');
                                $(all_div).find('input[name="kladr_district"]').val('');
                                for(var i in obj.parents){
                                    if (obj.parents[i].typeShort == 'обл')
                                    {
                                        $(all_div).find('input[name="kladr_region"]').val(obj.parents[i].typeShort + '. ' + obj.parents[i].name);
                                    }
                                    if (obj.parents[i].typeShort == 'р-н')
                                    {
                                        $(all_div).find('input[name="kladr_district"]').val(obj.parents[i].typeShort + '. ' + obj.parents[i].name);
                                    }
                                }
                                $(all_div).find('input[name="kladr_street"]').kladr('option', { parentType: $.ui.kladrObjectType.CITY, parentId: ui.item.obj.id } );
                                $(all_div).find('[name="kladr_city"]').css('color','');
                            }
                });
                this.$('[name="kladr_city"]').change(function(){
                        var all_div = $(this).closest('div[name="kladr_address"]')[0];
                        var city = $(all_div).find('[name="kladr_city"]');
                        var street = $(all_div).find('[name="kladr_street"]');
                        var building = $(all_div).find('[name="kladr_house"]');
                        $.kladrCheck({
                            token: kladr_token,
                            key: kladr_key,
                            value: city.val(),
                            type: $.ui.kladrObjectType.CITY,
                            withParents: true,
                        }, function(obj){
                            if(obj) {
                                city.val(obj.typeShort + '. ' + obj.name);
                                city.data( "kladr-obj", obj );
                                city.parent().find( 'label' ).text( obj.type );
                                street.kladr( 'option', { parentType: $.ui.kladrObjectType.CITY, parentId: obj.id } );
                                building.kladr( 'option', { parentType: $.ui.kladrObjectType.CITY, parentId: obj.id } );
                                city.css('color','');
                                for(var i in obj.parents){
                                    if ((obj.parents[i].typeShort == 'обл') || (obj.parents[i].type == 'Республика'))
                                    {
                                        $(all_div).find('input[name="kladr_region"]').val(obj.parents[i].typeShort + '. ' + obj.parents[i].name);
                                    }
                                    if (obj.parents[i].typeShort == 'р-н')
                                    {
                                        $(all_div).find('input[name="kladr_district"]').val(obj.parents[i].typeShort + '. ' + obj.parents[i].name);
                                    }
                                }
                            } else {
                                city.data( "kladr-obj", null );
                                //city.css('color', 'red');
                            }   
                        });
                    });
            }
            else{
                this._super();
            }

        },
    });
    instance.web.form.widgets.add('kladr_region', 'instance.web_kladr_widget.kladr_regionWidget');
    instance.web_kladr_widget.kladr_regionWidget = instance.web.form.FieldChar.extend({
        template: "kladr_region",

        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
                this.$('[name="kladr_region"]').kladr({
                    token: kladr_token,
                    key: kladr_key,
                    type: $.ui.kladrObjectType.REGION,
                    withParents: true,
                    select: function( event, ui ){
                                var obj = ui.item.obj;
                                ui.item.value = obj.typeShort + '. ' + ui.item.value;

                                var all_div = $(this).closest('div[name="kladr_address"]')[0];
                                
                                $(all_div).find('input[name="kladr_district"]').kladr('option', { parentType: $.ui.kladrObjectType.REGION, parentId: ui.item.obj.id } );
                                $(all_div).find('input[name="kladr_city"]').kladr('option', { parentType: $.ui.kladrObjectType.REGION, parentId: ui.item.obj.id } );
                                $(all_div).find('input[name="kladr_street"]').kladr('option', { parentType: $.ui.kladrObjectType.REGION, parentId: ui.item.obj.id } );
                            }
                });
            
            }
            else{
                this._super();
            }

        },
    });
    instance.web.form.widgets.add('kladr_district', 'instance.web_kladr_widget.kladr_districtWidget');
    instance.web_kladr_widget.kladr_districtWidget = instance.web.form.FieldChar.extend({
        template: "kladr_district",
        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
                this.$('[name="kladr_district"]').kladr({
                    token: kladr_token,
                    key: kladr_key,
                    type: $.ui.kladrObjectType.DISTRICT,
                    withParents: true,
                    label: function(obj, query){
                            var result = '';
                            for(var i in obj.parents){
                                result += obj.parents[i].typeShort + '. ' + obj.parents[i].name + ', ';
                            }
                            result += obj.typeShort + '. ' + obj.name;
                            return result;
                        },
                    select: function( event, ui ){
                                var obj = ui.item.obj;
                                ui.item.value = obj.typeShort + '. ' + ui.item.value;
                                var all_div = $(this).closest('div[name="kladr_address"]')[0];
                                
                                for(var i in obj.parents){
                                    
                                    if (obj.parents[i].typeShort == 'обл')
                                    {
                                        $(all_div).find('input[name="kladr_region"]').val(obj.parents[i].typeShort + '. ' + obj.parents[i].name);
                                    }
                                    
                                }
                                $(all_div).find('input[name="kladr_city"]').kladr('option', { parentType: $.ui.kladrObjectType.DISTRICT, parentId: ui.item.obj.id } );
                                $(all_div).find('input[name="kladr_street"]').kladr('option', { parentType: $.ui.kladrObjectType.DISTRICT, parentId: ui.item.obj.id } );
                            }

                });
            }
            else{
                this._super();
            }

        },
    });
    instance.web.form.widgets.add('kladr_street', 'instance.web_kladr_widget.kladr_streetWidget');
    instance.web_kladr_widget.kladr_streetWidget = instance.web.form.FieldChar.extend({
        template: "kladr_street",
        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
                this.$('[name="kladr_street"]').kladr({
                    token: kladr_token,
                    key: kladr_key,
                    type: $.ui.kladrObjectType.STREET,
                    withParents: true,
                    select: function( event, ui ){
                                var obj = ui.item.obj;
                                ui.item.value = obj.typeShort + '. ' + ui.item.value;
                                var all_div = $(this).closest('div[name="kladr_address"]')[0];
                                $(all_div).find('input[name="kladr_house"]').kladr('option', { parentType: $.ui.kladrObjectType.STREET, parentId: ui.item.obj.id } );
                            }

                });
            }
            else{
                this._super();
            }

        },
    });
    instance.web.form.widgets.add('kladr_house', 'instance.web_kladr_widget.kladr_houseWidget');
    instance.web_kladr_widget.kladr_houseWidget = instance.web.form.FieldChar.extend({
        template: "kladr_house",
        render_value: function() {
            if (!this.get("effective_readonly")) {
                this._super();
                this.$('[name="kladr_house"]').kladr({
                    token: kladr_token,
                    key: kladr_key,
                    type: $.ui.kladrObjectType.BUILDING,
                    withParents: true,
                    select: function( event, ui ){
                                var obj = ui.item.obj;
                                ui.item.value = obj.typeShort + '. ' + ui.item.value;
                                var all_div = $(this).closest('div[name="kladr_address"]')[0];
                                $(all_div).find('input[name="kladr_zip"]').val(obj.zip);
                            }

                });
            }
            else{
                this._super();
            }

        },
    });
    instance.web.form.widgets.add('kladr_zip', 'instance.web_kladr_widget.kladr_zipWidget');
    instance.web_kladr_widget.kladr_zipWidget = instance.web.form.FieldChar.extend({
        template: "kladr_zip",
        render_value: function() {
                this._super();
        },
    });
};
