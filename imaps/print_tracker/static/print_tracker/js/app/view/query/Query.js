/*
* Query panel layout
*/
Ext.define('APP.view.query.Query',{
	extend: 'Ext.panel.Panel',
	alias: 'widget.query',
	title: 'Query tool',
	width: 190,
	/*
	* Define comboboxes for the selections and assign them the stores
	*/
	items: [
		{
			xtype:'combobox',
			displayField: 'name',
			id: 'unitSelector',
			valueField: 'name',
			emptyText: 'Select a Unit',
			store: 'Units'
		},{
			xtype:'combobox',
			id: 'yearSelector',
			displayField: 'num',
			valueField: 'num',
			emptyText: 'Select a Year',
			store: 'Years'
		},{
			xtype:'combobox',
			id: 'monthSelector',
			displayField: 'name',
			valueField: 'num',
			emptyText: 'Select a Month',
			store: 'Months'
		}
	]
});