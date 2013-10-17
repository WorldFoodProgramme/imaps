from models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json

def init(request):
    """Main function to serve the application responses"""
    if request.method == 'GET':
	return render_to_response('wwatch/index.html', {}, RequestContext(request))

def JSONSerializer(request, object):
	jsontpl = {
	"type": "FeatureCollection",
	"features":[],
	}
	"""Serializes a queryset or object into json"""
	if request.method=='GET':
	    if object=='Events':
	        for item in Event.objects.all():
		    if item.visible:
			    p = Resource.objects.filter(event__id=item.id)	
			    l = Link.objects.filter(event__id=item.id)
			    c = 0
			    d = 0
			    itemTPL={}
			    itemProperties={}
			    itemGeometry={}
			    itemTPL['type'] = "Feature"	
			    itemTPL['id'] = item.id
			    itemGeometry['type'] = "MultiPolygon"
			    itemGeometry['coordinates'] = item.country.mpoly.tuple
			    itemProperties['country'] = item.country.terr_name		
			    itemProperties['alert_level'] = item.alert_level
			    itemProperties['hazard_type'] = item.hazard_type
			    itemProperties['date'] = item.date.isoformat()
			    itemProperties['comment'] = item.event_comment
			    for item2 in p:
			        itemProperties['doc'+ str(c)] = item2.name
			        itemProperties['url'+ str(c)] = item2.document.url
				c+=1
			    for item3 in l:
			        itemProperties['link'+ str(d)] = item3.link
				d+=1
			    itemTPL["properties"]=itemProperties
			    itemTPL["geometry"]=itemGeometry
			    jsontpl["features"].append(itemTPL)
		    

	        response = HttpResponse(json.dumps(jsontpl, ensure_ascii=False))
		return response

	elif request.method=='POST':
	    return HttpResponse('Sorry no POST requests allowed for JSON serialization')

