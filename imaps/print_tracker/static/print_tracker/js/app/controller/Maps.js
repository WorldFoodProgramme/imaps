/*
* Controller for the Maps section which is the list of results in the center of the page
*/
Ext.define('APP.controller.Maps',{
	extend: 'Ext.app.Controller',
	stores: [
		'Maps'
	],
	models: ['Map'],
	views: [
		'map.List'
	],
	init: function(){
		var store = this.getStore('Maps');
		store.addListener('datachanged',this.updateTotalCost,this,store);
	},
	/*
	* Updates the bottom bar with the total cost of the displayed maps
	*/
	updateTotalCost: function(store){
		var total = 0;
		store.each(function(record){
			total += record.data.cost;
		});
		var el = new Ext.Element(Ext.DomQuery.selectNode('#total_cost')).update(Math.round(total*10)/10);
	}
});