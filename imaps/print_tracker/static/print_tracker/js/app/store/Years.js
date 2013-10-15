/*
* Map store. Ajax request
*/
Ext.define('APP.store.Years',{
	extend: 'Ext.data.Store',
	model: 'APP.model.Year',
	autoLoad: true,
	proxy: {
		type: 'ajax',
		api: {
			read: '/years'
		},
		reader: {
			type: 'json',
			root: 'years',
			successProperty: 'success'
		}
	}
});