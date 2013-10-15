/*
* Unit store. Ajax request
*/
Ext.define('APP.store.Units',{
	extend: 'Ext.data.Store',
	model: 'APP.model.Unit',
	autoLoad: true,
	proxy: {
		type: 'ajax',
		api: {
			read: '/units'
		},
		reader: {
			type: 'json',
			root: '',
			record:'fields',
			successProperty: 'success'
		}
	}
});