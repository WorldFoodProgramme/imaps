# django
import unicodecsv
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.gis.shortcuts import render_to_kml
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from imaps import settings
# application
from models import Feed, Item, Place, Person, Domain, Keyword, Filter, Tweet, Search
from gdelt.models import Event
#from forms import PlaceForm

@login_required
def filters(request):
    """
    View a full list of the filters, and form for updating them.
    """
    # TODO for now we have just one filter containing all the keywords
    filters = Filter.objects.all()[0]
    instance = FilterForm.Meta.model.objects.get(pk=filters.id)
    form = FilterForm(instance=instance)
    # if it is a POST then we need to update the filter
    if request.method == 'POST': # POST
        form = FilterForm(request.POST, instance=instance)
        try:
            model = form.save()
            filter_items()
        except ValueError:
            pass
    return render_to_response('feeds/filter_list.html',
            {'form': form, },
            RequestContext(request))

def filter_items():
    """
    Filter all unarchive items based on the filters.
    """
    import re
    keywords = Filter.objects.all()[0].keywords
    keywords = keywords.splitlines()
    items = Item.objects.filter(archived=False)
    for item in items:
        text2filter = item.title + item.summary
        combined = "(" + ")|(".join(keywords) + ")"
        if re.search(combined, text2filter, re.IGNORECASE):
            print('\n***Item is going to be filtered!\n')
            item.filtered = True
        else:
            item.filtered = False
        item.save()

def get_kml_places(request):
    """
    View for generating kml for countries.
    """
    places = Place.objects.kml()
    return render_to_kml("gis/kml/placemarks.kml", {'places' : places})

@login_required
def item_archive(request, id):
    """
    Archive/Unarchive an Item
    """
    item = Item.objects.get(pk=id)
    print 'archiving item %s' % item.id
    status = 'archived'
    if item.archived:
        item.archived = False
        status = 'unarchived'
        if item.filtered:
            status = 'filtered'
    else:
        item.archived = True
    item.save()
    return HttpResponse(status)

def list_feeds_for_class(request, feedclass):
    """
    List the feeds name given a class.
    """
    feeds = Feed.objects.all()
    if feedclass != 'ALL':
        feeds = feeds.filter(feed_class=feedclass)
    print 'listing feeds for class: %s' % feedclass
    result = []
    for feed in feeds:
        result.append({"id":feed.id, "name":feed.name, "unarchived": feed.unarchived()})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

# item

def tweets_map(request):
    """
    View a series of places on a map.
    """
    # TODO
    #if 'tag' in request.GET:
    #    tag = request.GET.get('tag', '')
    #    tweets = tweets.filter(tags__name__in=[tag])
    #    search_name = 'all searches'
    rcount = 200
    tweets = None
    places = None
    if 'search_id' in request.GET:
        search_id = request.GET.get('search_id', '')
        search = Search.objects.get(id=search_id)
        tweets = Tweet.objects.filter(search=search).order_by('-created_at')[:rcount]
        places = Place.objects.filter(tweet__search__id=search_id)[:rcount]
        search_name = search.name
    else:
        tweets = Tweet.objects.all().order_by('-created_at')[:rcount]
        places = Place.objects.all()[:rcount]
        search_name = 'All searches'
        map_title = 'All searches'
    map_title = search_name
    search_text = 'Latest %s tweets items from %s' % (len(tweets), search_name)
    return render_to_response('items/item_map.html', 
        {   
            'tweets': tweets,
            'places': places,
            'search_name': search_name,
        },
        context_instance=RequestContext(request))

def tweets_list(request):
    """
    View a full list of tweets.
    """
    tweets = Tweet.objects.all().order_by('-created_at')
    return render_to_response('items/item_list.html', 
        {   
            'tweets' : tweets,
        },
        context_instance=RequestContext(request))
    
def tweets_list_csv(request):
    """
    Export a full list of tweets to csv.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tweets_export.csv"'

    tweets = Tweet.objects.all().order_by('-created_at')
    writer = unicodecsv.writer(response, encoding='utf-8')
    for t in tweets:
        writer.writerow([t.created_at, t.screen_name, t.status, t.the_places()])
    return response

def tweet_detail(request, id):
    """
    Item detail for a given pk.
    """
    tweet = get_object_or_404(Tweet, pk=id)
    return render_to_response('items/item_detail.html',
            {'tweet': tweet, },
            RequestContext(request))
            
# place

def places_list(request):
    """
    View a full list of places.
    """
    places = Place.objects.all()
    return render_to_response('places/place_list.html', 
        {
            'places': places,
        },
        context_instance=RequestContext(request))
        
def searches_list(request):
    """
    View a full list of searches.
    """
    searches = Search.objects.all()
    return render_to_response('searches/search_list.html', 
        {
            'searches': searches,
        },
        context_instance=RequestContext(request))

def place_detail(request, place_slug):
    """
    Place detail for a given name.
    """
    place = get_object_or_404(Place, slug=place_slug)
    return render_to_response('places/place_detail.html',
            {'place': place},
            RequestContext(request))
            
# person

def people_list(request):
    """
    View a full list of people.
    """
    people = Person.objects.all()
    return render_to_response('people/people_list.html', 
        {
            'people': people,
        },
        context_instance=RequestContext(request))

def person_detail(request, person_slug):
    """
    Person detail for a given name.
    """
    person = get_object_or_404(Person, slug=person_slug)
    return render_to_response('people/person_detail.html',
            {'person': person, },
            RequestContext(request))
            
# domain

def domains_list(request):
    """
    View a full list of domains.
    """
    domains = Domain.objects.all()
    return render_to_response('domains/domain_list.html', 
        {
            'domains': domains,
        },
        context_instance=RequestContext(request))

def domain_detail(request, id):
    """
    Domain detail for a given pk.
    """
    domain = get_object_or_404(Domain, pk=id)
    return render_to_response('domains/domain_detail.html',
            {'domain': domain, },
            RequestContext(request))
            
# keyword

def keyword_detail(request, keyword_name):
    """
    Keyword detail for a given name.
    """
    keyword = get_object_or_404(Keyword, name=keyword_name)
    return render_to_response('keywords/keyword_detail.html',
            {'keyword': keyword, },
            RequestContext(request))
            
# tag

def tags_list(request):
    """
    View a full list of tags.
    """
    return render_to_response('tags/tag_list.html', 
        {
        },
        context_instance=RequestContext(request))

def tag_detail(request, tag_slug):
    """
    Tag detail for a given name.
    """
    items = Item.objects.filter(tags__name__in=[tag_slug])
    return render_to_response('tags/tag_detail.html',
            {'tag_slug': tag_slug,
             'items': items, },
            RequestContext(request))
    
# test method
def test(request):
    """
    A view for test.
    """
    num_news = 10
    return render_to_response('others/test.html', 
        {'num_news' : num_news},
        RequestContext(request))
        
