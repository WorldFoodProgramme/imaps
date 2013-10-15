/*
* Map store. Ajax request
*/
Ext.define('APP.store.Maps',{
	extend: 'Ext.data.Store',
	model: 'APP.model.Map',
	autoLoad: false,
	proxy: {
		type: 'ajax',
		api: {
			read: '/report/'
		},
		reader: {
			type: 'json',
			root: 'items',
			successProperty: 'success'
		}
	}
});