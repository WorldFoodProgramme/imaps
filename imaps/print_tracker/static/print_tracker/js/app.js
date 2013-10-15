/*
* Main application
* Creates the main layout of the page and binds together the views and the controllers
*/
Ext.require('Ext.container.Viewport');
Ext.application({
    name: 'APP',
	folder: 'app',
	appFolder: '/media/js/app',
	/*
	* Method execute on lounch of the app
	*/
    launch: function() {
		new Ext.Element(Ext.DomQuery.selectNode('#loading')).setStyle('display','none');
        Ext.create('Ext.container.Viewport', {
            layout: 'border',
            items:
			[{
            	region: 'north',
				xtype: 'panel',
				heigth: 100,
				html: 'OMRT'
            },
			{
            	region: 'west',
				xtype: 'query'
            },
			{
            	region: 'center',
				xtype: 'maplist'
            }]
        });
    },
	controllers: [
		'Maps',
		'Queries'
	]
});