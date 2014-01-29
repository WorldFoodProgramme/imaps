from models import *
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json

def init(request):
    """Main function to serve the application responses"""
    if request.method == 'GET':
        events = Event.objects.all().filter(visible = True).order_by('country__terr_name')
        return render_to_response(
            'wwatch/index.html', 
            {'events': events}, 
            RequestContext(request)
        )

def getEvents(request):
    jsontpl = {
        "type": "FeatureCollection",
        "features":[],
    }
    """Serializes a queryset or object into json"""
    if request.method=='GET':
        for item in Event.objects.all():
            if item.visible:
                resources = Resource.objects.filter(event__id=item.id)
                links = Link.objects.filter(event__id=item.id)
                itemTPL={}
                itemProperties={}
                itemGeometry={}
                itemResources={}
                itemTPL['type'] = "Feature"
                itemTPL['id'] = item.id
                itemGeometry['type'] = "MultiPolygon"
                itemGeometry['coordinates'] = item.country.mpoly.tuple
                itemProperties['country'] = item.country.terr_name
                itemProperties['alert_level'] = item.alert_level
                itemProperties['hazard_type'] = item.hazard_type
                if(item.confidence is not None):
                    itemProperties['confidence'] = item.get_confidence_display()
                else:
                    itemProperties['confidence'] = "N/A"
                itemProperties['date'] = item.date.isoformat()
                itemProperties['comment'] = item.event_comment
                #import ipdb;ipdb.set_trace()
                itemTPL["properties"]=itemProperties
                itemTPL["geometry"]=itemGeometry
                itemLinks = []
                itemResources = []
                for link in links:
                    itemLink={}
                    itemLink['id'] = link.id
                    itemLink['link'] = link.link
                    itemLinks.append(itemLink)
                for resource in resources:
                    itemResource={}
                    itemResource['name'] = resource.name
                    itemResource['url'] = resource.document.url
                    itemResources.append(itemResource)
                itemTPL["links"]=itemLinks
                itemTPL["resources"]=itemResources
                jsontpl["features"].append(itemTPL)
                
        #import ipdb;ipdb.set_trace()
        response = HttpResponse(json.dumps(jsontpl, ensure_ascii=False))
        return response
    elif request.method=='POST':
        return HttpResponse('Sorry no POST requests allowed for JSON serialization')


