from capro.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json

def init(request):
	"""Main function to serve the application responses"""
	if request.method == 'GET':
		return render_to_response('capro/index.html')

def JSONSerializer(request):
	jsontpl = {
	    "type": "FeatureCollection",
	    "features":[],
	}
	"""Serializes a queryset or object into json"""
	if request.method=='GET':
		for item in Country.objects.all():
			p = Profile.objects.filter(country__id=item.id)
			c = 0						
			itemTPL={}
			itemProperties={}	
			itemGeometry={}			
			itemTPL['type'] = "Feature"	
			itemTPL['id'] = item.id
			itemGeometry['type'] = "Point"
			itemGeometry['coordinates'] = [item.point.x, item.point.y]
			itemProperties['name'] = item.get_name_display()	
			itemProperties['regional'] = item.get_regional_display()	
			itemProperties['ndmo'] = item.ndmo
			itemProperties['reporting_line'] = item.reporting_line
			itemProperties['address'] = item.address
			itemProperties['focal_point'] = item.focal_point
			itemProperties['contacts'] = item.contacts
			itemProperties['wfp_focal_point'] = item.wfp_focal_point
			for item2 in p:
				itemProperties['doc'+ str(c)] = item2.name
				itemProperties['url'+ str(c)] = item2.document.url
				c+=1
			itemTPL["properties"]=itemProperties
			itemTPL["geometry"]=itemGeometry
			jsontpl["features"].append(itemTPL)
		response = HttpResponse(json.dumps(jsontpl, ensure_ascii=False))
		return response

	elif request.method=='POST':
		return HttpResponse('Sorry no POST requests allowed for JSON serialization')
			
	
		
