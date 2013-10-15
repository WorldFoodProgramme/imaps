# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from models import MapCopy, Unit
import datetime
import json
from django.db.models import Q
from django.template import RequestContext
from django.core import serializers
from django.conf import settings

def init(req):
	"""Initial view, just renders the index.html"""
	return render_to_response('print_tracker/index.html',{},RequestContext(req))
	
def mapReport(req,unit=None,year=None,month=None):
	"""
	Controller for reports, it accets the following queries:
	
	/unit -> query by unit
	/unit/year -> query by unit and year
	/unit/year/month -> query by unit, year and month
	/year -> query by year
	/year/month -> query by year and month
	
	The result is in JSON format
	
	No POST requests allowed
	
	"""
	result = {
		'success' : True,
		'items' : []
	}
	
	if req.method == 'GET':
		maps = MapCopy.objects
		try: 
			unit = Unit.objects.get(name=unit)
		except Unit.DoesNotExist:
			"""Silently except if no unit passed"""
			pass 
		if unit is not None and year is not None and month is not None:
			maps = maps.filter(Q(unit=unit) & Q(date__year=year) & Q(date__month=month))
		elif unit is not None and year is not None:
			maps = maps.filter(Q(unit=unit) & Q(date__year=year))
		elif year is not None and month is not None:
			maps = maps.filter(Q(date__year=year) & Q(date__month=month))
		elif year is not None: 
			maps = maps.filter(Q(date__year=year))
		else:
			maps = maps.filter(Q(unit=unit))
		for mapcopy in maps:
			if mapcopy.number != 0:
				maptpl = {}
				cost = getCost(mapcopy.copy.format,mapcopy.number)
				maptpl['title'] = mapcopy.copy.map.title
				maptpl['format'] = mapcopy.copy.format.name
				maptpl['copies'] = mapcopy.number
				maptpl['date'] = mapcopy.date.isoformat()
				maptpl['cost'] = cost
				result['items'].append(maptpl)
			
		return HttpResponse(json.dumps(result))
	else: return HttpResponse(status=403)

def getUnits(req):
	"""Return the JSON list of the units available in the databse"""
	return HttpResponse(serializers.serialize('json',Unit.objects.all()))
	
def getYears(req):
	"""Returns a JSON of the years in where the copies have been printed"""
	result = {
		'success' : True,
		'years' : [dict([('num',date.year)]) for date in MapCopy.objects.dates('date','year')],
	}
	return HttpResponse(json.dumps(result))

def getCost(format,copies):
	"""
	Calculate the cost for each MapCopy event.
	The cost is based on the fixed cost from the settings plus the format cost, all multiplied by the number of copies in the event.
	"""
	if format.cost:
	    costPerCopy = settings.MAP_COST + format.cost
	else:
	    costPerCopy = 0
	return round(costPerCopy * copies,1) 
