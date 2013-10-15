/*
* Map store. Local data.
*/
Ext.define('APP.store.Months',{
	extend: 'Ext.data.ArrayStore',
	model: 'APP.model.Month',
	data: [[
	'January',1
	],[
	'February',2
	],[
	'March',3
	],[
	'April',4
	],[
	'May',5
	],[
	'June',6
	],[
	'July',7
	],[
	'August',8
	],[
	'September',9
	],[
	'October',10
	],[
	'November',11
	],[
	'December',12
	]]
});