/*
* Controller for the Queries section which is the list of three comboboxes in the right column
*/
Ext.define('APP.controller.Queries',{
	extend: 'Ext.app.Controller',
	views: [
		'query.Query',
	],
	models: ['Unit','Year','Month'],
	stores:['Units','Years','Months'],
	/*
	* Attach a onChange listener on each of the combobox widgets
	*/
	init: function(){
		this.control({
			'combobox':{
				change: function(sender,newValue,oldValue){
					this.onQueryChange(sender,newValue);
				}
			}
		});
	},
	/*
	* Action performed when a change event is triggered
	* Creates a new URL for the reader of the store
	*/
	onQueryChange: function(sender,newValue){
		var store = Ext.ComponentQuery.query('.maplist')[0].getStore();
		var url = this.buildApiUrl(this.collectQueryValues());
		if(url != '#'){
			store.getProxy().api.read = '/report/'+url;
			store.load();
		};
	},
	/*
	* Helper method for collecting the actual values from the comboboxes widgets
	*/
	collectQueryValues: function(){
		var comboboxes = Ext.ComponentQuery.query('.combobox');
		var values = {};
		for(var i=0;i<comboboxes.length;i++){
			values[comboboxes[i].id]=comboboxes[i].getValue();
		}
		return values;
	},
	/*
	* Builder method for creating the proper URL based on the three values of the comboboxes
	*/
	buildApiUrl: function(values){
		var url = '#';
		var unit = values.unitSelector;
		var year = values.yearSelector;
		var month = values.monthSelector;
		if(unit){
			if(year){
				if(month){
					url = [unit,year,month].join('/');
				}
				else if(!month){
					url = [unit,year].join('/');
				}
			}
			else if(!year){
				url = unit;
			}
		}
		else if(!unit && year){
			if(month){
				url = [year,month].join('/');
			}
			else if (!month){
				url = year;
			}
		}
		return url;	
	}
});