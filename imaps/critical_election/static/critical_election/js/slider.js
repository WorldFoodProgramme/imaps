
	var today = new Date();
	var start_date = new Date(2011, 1, 1);
	var months = new Array("January","February","March","April","May","June","July","August","September","October","November","December");
	var maxDaysMonths = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
	var START_YEAR = 2011;
	var START_MONTH = 1;
	var NB_MONTHS = 12;

	function monthDiff(d1, d2) {
	// return the difference in months between 2 dates
		var months;
		months = (d2.getFullYear() - d1.getFullYear()) * NB_MONTHS;
		months -= d1.getMonth() + 1;
		months += d2.getMonth();
		return months;
	}

	function dateSlider(index) {
	// return the current date of the slider at the index "index" (0 for value min, 1 for value max)	
		if (index > 1) {
			var d = new Date(START_YEAR,0,START_MONTH);
		}
		else {
			var d = new Date(START_YEAR+parseInt($("#slider").slider("values", index)/NB_MONTHS), $("#slider").slider("values", index)%NB_MONTHS,1);
		}
		if (index = 1) {
			d.setDate(maxDaysMonths[$("#slider").slider("values", index)%NB_MONTHS]);
		}
		return d;
	}

	$(function(){
	// Slider		
		$("#slider").slider({
			range: true,
			min: 0,
			max: (today.getFullYear()-START_YEAR)*NB_MONTHS + today.getMonth() + NB_MONTHS-1,
			values: [monthDiff(start_date, today)+2, monthDiff(start_date, today)+NB_MONTHS+1],
			step: 1,
			stop: function(event, ui) {
				  // executed while user stop sliding
				  //$("#period").val(ui.values[0] + " to " + ui.values[1]);
					$("#period").val(months[parseInt((ui.values[0])%NB_MONTHS)] + " " + (START_YEAR+parseInt(ui.values[0]/NB_MONTHS)) + " to " + months[parseInt((ui.values[1])%NB_MONTHS)] + " " + (START_YEAR+parseInt(ui.values[1]/NB_MONTHS)));										
					layerRefresh();						// refresh the content of the map
				}
		});
		//$("#period").val($("#slider").slider("values", 0) + " to " + $("#slider").slider("values", 1));
		$("#period").val(months[$("#slider").slider("values", 0)%NB_MONTHS] + " " + today.getFullYear() + " to " + months[$("#slider").slider("values", 1)%NB_MONTHS] + " " + (today.getFullYear()+1));
	});


