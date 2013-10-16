from critical_election.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core import serializers
from critical_election.serializers import json as jsonSerializer
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import json
    
def init(req):
	"""Main function to serve the application responses"""
	if req.method == 'GET':
		return render_to_response('critical_election/index.html')

def JSONSerializer(req,object):
	jsontpl = {
	"type": "FeatureCollection",
	"features":[],
	}
	"""Serializes a queryset or object into json"""
	if req.method=='GET':
		if object=='Elections':
			for item in Election.objects.all(): #Election.objects.filter(election_date_start__gt='2012-10-01'):
				all_updates = Update.objects.filter(election__id=item.id).order_by('-update_date')
				i = 0						

				itemTPL={}
				itemProperties={}
				itemGeometry={}
				itemTPL['type'] = "Feature"
				itemTPL['id'] = item.id
				itemGeometry['type'] = "MultiPolygon"
				itemGeometry['coordinates'] = item.country.mpoly.tuple
				itemProperties['country'] = item.country.terr_name
				itemProperties['type'] = item.election_type
				if item.election_date_start:
					itemProperties['date_start'] = item.election_date_start.isoformat()
				itemProperties['date_text'] = item.election_date_text
				if item.election_date_end:
					itemProperties['date_end'] = item.election_date_end.isoformat()
				if item.election_date_estimation:
					itemProperties['date_estimation'] = item.election_date_estimation.isoformat()
				itemProperties['comment'] = item.election_comment
				for item2 in all_updates:
					itemProperties['date_update'+ str(i)] = item2.update_date.isoformat()
					itemProperties['description_update'+ str(i)] = item2.update_description
					itemProperties['source_update'+ str(i)] = item2.update_source
					i+=1
				itemProperties['number_updates'] = i
				itemTPL['properties']=itemProperties
				itemTPL['geometry']=itemGeometry
				jsontpl['features'].append(itemTPL)

		elif object=='lastUpdates':
			updates = Update.objects.order_by('election__country__terr_name')
			#for item in updates.filter(update_date=updates.order_by('-update_date')[0].update_date).order_by('election.country'):
			# get only the last updates (order updates by date desc and get the maximum date
			for item in updates.filter(update_date=updates.aggregate(dateMax=Max('update_date'))['dateMax']):
				
				itemTPL={}
				itemProperties={}
				itemTPL['id'] = item.id
				itemProperties['country'] = item.election.country.terr_name
				itemProperties['election_type'] = item.election.election_type
				if item.election.election_date_start:
					itemProperties['election_date_start'] = item.election.election_date_start.isoformat()
				if item.election.election_date_end:
					itemProperties['election_date_end'] = item.election.election_date_end.isoformat()
				if item.election.election_date_estimation:
					itemProperties['election_date_estimation'] = item.election.election_date_estimation.isoformat()
				itemProperties['election_date_text'] = item.election.election_date_text
				itemProperties['date_update'] = item.update_date.isoformat()
				itemProperties['description_update'] = item.update_description
				itemProperties['source_update'] = item.update_source
				itemTPL['properties']=itemProperties
				jsontpl['features'].append(itemTPL)	

		response = HttpResponse(json.dumps(jsontpl, ensure_ascii=False))
		return response

	elif req.method=='POST':
	    return HttpResponse('Sorry no POST requests allowed for JSON serialization')


