
	var center = new L.LatLng(10, 12);
    var map = L.map('map').setView(center, 3);
    L.tileLayer('http://{s}.tile.cloudmade.com/{key}/{styleId}/256/{z}/{x}/{y}.png', {
				//http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png
		key: 'BC9A493B41014CAABB98F0471D759707',
		styleId: 22677,
		minZoom: 2,	
		maxZoom: 5,
		attribution: ''
    }).addTo(map);

	//////////////////////////////////////////////////////////
    // Create empty layers where we will load the polygons
    electionLayer = new L.GeoJSON();
        
	//////////////////////////////////////////////////////////
	function style(feature) {
	// modify the style according to the type of election
		switch(feature.properties.type) {
			case "Presidential": return presidentialStyle;
			case "Parliamentary": return parliamentaryStyle;
			case "Presidential / Parliamentary": return presparlStyle;
			case "Referendum": return referendumStyle;
			case "Local Election": return localStyle;
			default: return defaultStyle;
		}
	}

	function highlightStyle(e) {
	// modify the style according to the type of election		
		switch(e.target.properties.type) {
			case "Presidential": return presidentialFocusStyle;
			case "Parliamentary": return parliamentaryFocusStyle;
			case "Presidential / Parliamentary": return presparlFocusStyle;
			case "Referendum": return referendumFocusStyle;
			case "Local Election": return localFocusStyle;
			default: return defaultStyle;
		}
	}

	//////////////////////////////////////////////////////////
	function highlightFeature(e) {
	// Highlight a feature onmouve over
		e.target.setStyle(highlightStyle(e));
	}

	function resetHighlightFeature(e) {
	// reset to the normal style    	
		e.target.setStyle(style(e.target));
	}

	//////////////////////////////////////////////////////////
	function displayUpdates(e) {
	// on event click display updates in the right panel
		//highlightFeature(e);		
		html_string = '<script type="text/javascript">$(function() { $("#accordion").accordion({ autoHeight: false, event: "mouseover"});});</script><input type="text" id="country_updates" value="" readonly="readonly" style="border:0; background-color:#f2f5f7; color:#404040; font-weight:bold; font-size:22px"/><br><br><div id="accordion">';		// html text for the accordion div
		i = 0;		
		while (i < e.target.properties.number_updates) {
		// get all updates for the current couple {country / election}
			current_date = 'e.target.properties.date_update'+i;
			current_description = 'e.target.properties.description_update'+i;
			current_source = 'e.target.properties.source_update'+i;		
			html_string = html_string + '<div><a href="#">Updates of ' + eval(current_date) + '</a></div><div><font size="2"><u>Description:</u> ' + eval(current_description) + '</font><p><font size="1"><i><a href="' + eval(current_source) + '" target="_blank">Sources</a></i></font></p></div>';
			i++;
		}
	
		html_string = html_string + '</div></div>';
		$("#updates_selected").html(html_string);
		$("#country_updates").val(e.target.properties.country);		// update the country

	}

	//function zoomToFeature(e) {
		//map.fitBounds(e.target.getBounds());
	//}

	//////////////////////////////////////////////////////////
	function onEachFeature(feature, layer) {
		layer.properties = feature.properties;
		layer.on({
			target: layer.bindPopup("<h2 style='color:SteelBlue;font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:16px;'>" + feature.properties.country + "</h2><hr color=LightSteelBlue><table border='0'><tr><td width='120'><style='font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:12px;'><b><i>Type:  </i></b></td><td>" + feature.properties.type + "</td></tr><tr><td><style='font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:12px;'><b><i>Date (first round):  </i></b></td><td>" + feature.properties.date_start + "</td></tr><tr><td><style='font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:12px;'><b><i>Date (planned):  </i></b></td><td>" + feature.properties.date_text + "</td></tr><tr><td><style='font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:12px;'> <b><i>Date (second round):  </i></b></td><td>" + feature.properties.date_end + "</td></tr><tr><td><style='font-family:Lucida Grande, Lucida Sans, Arial, sans-serif;font-size:12px;'> <b><i>Comment:  </i></b></td><td>" + feature.properties.comment + "</td></tr></table>"),
			mouseover: highlightFeature,
			mouseout: resetHighlightFeature,
			click: displayUpdates,
			//click: zoomToFeature,
		})
	}


	//////////////////////////////////////////////////////////
	function pad(n){return n<10 ? '0'+n : n;}	// display number on n digits

	function ISODateString(d){
 		return d.getUTCFullYear()+'-' + pad(d.getUTCMonth()+1)+'-' + pad(d.getUTCDate())+'T' + pad(d.getUTCHours())+':' + pad(d.getUTCMinutes())+':' + pad(d.getUTCSeconds())+'Z'}


	//////////////////////////////////////////////////////////
	function mapFilter(feature, layer) {
	// apply a filter on feature according to the date of the election
		var d1 = new Date(dateSlider(0).getFullYear(), dateSlider(0).getMonth(), 1);
		var d2 = new Date(dateSlider(1).getFullYear(), dateSlider(1).getMonth(), dateSlider(1).getDate());

	return (feature.properties.date_start >= ISODateString(d1) && feature.properties.date_start <= ISODateString(d2)) || (feature.properties.date_end >= ISODateString(d1) && feature.properties.date_end <= ISODateString(d2)) || (
feature.properties.date_estimation >= ISODateString(d1) && feature.properties.date_estimation <= ISODateString(d2))
	}

	//////////////////////////////////////////////////////////
	function layerRefresh() {
	// refresh the layer in the map					
		jqxhr = $.getJSON("/imaps/CriticalElection/json/Elections", function(data) {	// get the Json Object		
			if(electionLayer) {
				map.removeLayer(electionLayer);
			}
			electionLayer = L.geoJson(data,{
				style: style,					// load the style of the objects define in the function style
				onEachFeature: onEachFeature,	// load events to apply to each feature
				filter: mapFilter				// load the filter on the layer
			}).addTo(map);						// add the geoJson to the map
		});
	}
	layerRefresh();

	//////////////////////////////////////////////////////////
	function lastUpdatesLoad() {
	// load the last updates in the tab					
		jqxhr = $.getJSON("/imaps/CriticalElection/json/lastUpdates", function(data) {	// get the Json Object					
			html_string = '<script type="text/javascript">$(function() { $("#current_updates_content").accordion({ autoHeight: false, event: "mouseover"});});</script><h4>Updates of ' + data.features[0].properties.date_update + '</h4><div id="current_updates_content">';

			i = 0;
			while(i < data.features.length) {			
				lu_date = data.features[i].properties.date_update;
				lu_country = data.features[i].properties.country;
				lu_type = data.features[i].properties.election_type;
				if (data.features[i].properties.election_date_start)		
					lu_date_election = data.features[i].properties.election_date_start;
				else if (data.features[i].properties.election_date_end)
					lu_date_election = data.features[i].properties.election_date_start;
				else
					lu_date_election = data.features[i].properties.election_date_text;
				lu_description = data.features[i].properties.description_update;
				lu_source = data.features[i].properties.source_update;		
				html_string = html_string + '<div><a href="#">' + lu_country + ' : <i>' + lu_type + ' - ' + lu_date_election + '</i></a></div><div><font size="2"><u>Description:</u> ' + lu_description + '</font><p><font size="1"><i><a href="' + lu_source + '" target="_blank">Sources</a></i></font></p></div>';
				i = i + 1;
			}
			html_string = html_string + '</div>';
			$("#current_updates").html(html_string);
		});
	}
	lastUpdatesLoad();


//////////////////////////////////////////////////////////////



			
