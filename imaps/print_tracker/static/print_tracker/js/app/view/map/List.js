/*
* Map list layout
*/
Ext.define('APP.view.map.List',{
	extend: 'Ext.grid.Panel',
	alias: 'widget.maplist',
	title: 'All Copies',
	store: 'Maps',
	/*
	* Define the columns of the grid and the bottom bar
	*/
	initComponent: function(){
		this.columns = [
			{header: 'Name', dataIndex: 'title', flex: 1},
			{header: 'Date', dataIndex: 'date', flex: 1},
			{header: 'Format', dataIndex: 'format', flex: 1},
			{header: 'Number of copies', dataIndex: 'copies', flex: 1},
			{header: 'Cost ($)', dataIndex: 'cost', flex: 1}
		];
		this.bbar = ['->',{
			xtype: 'panel',
			width: 150,
			html: 'Total Cost ($): <span id="total_cost">0</span>'
		}];
		this.callParent(arguments);
	}
});