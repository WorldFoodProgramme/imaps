from django.db import models
from django.contrib.gis.db import models
import datetime

class Resource(models.Model):
    name = models.CharField('Document name',blank = True, max_length=255)
    document = models.FileField('Document', upload_to='wwatch/pdf/')
    event = models.ForeignKey('Event')
    
    class Meta:
        verbose_name_plural='Resources'
        verbose_name= 'Resource'
    
    def natural_key(self):
        return self.name

    def __unicode__(self):
            return self.name

class Link(models.Model):
    link = models.URLField('Link', max_length=255)
    event = models.ForeignKey('Event')
    
    class Meta:
        verbose_name_plural='Links'
        verbose_name= 'Link'
    
    def natural_key(self):
        return self.link

    def __unicode__(self):
            return self.link

class Country(models.Model):

    iso_3 = models.CharField('ISO', max_length=50)
    status = models.CharField('Status', max_length=50)
    color_code = models.CharField('Color Code', max_length=5)
    terr_id = models.IntegerField('ID')
    terr_name = models.CharField('Name', max_length=250)
    shape_leng = models.FloatField('Length')
    shape_area = models.FloatField('Area')

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural='Countries'
        verbose_name= 'Country'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.terr_name

class Event(models.Model):

    CONFIDENCE_CHOICES = (
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High')
    )
    
    EVENT_TYPE_CHOICES = (
        ('Minor Event', 'Minor Event'),
        ('Moderate Event', 'Moderate Event'),
        ('Major Event', 'Major Event')
    )
    
    HAZARD_TYPE_CHOICES = (
        ('Drought', 'Drought'),
        ('Flood', 'Flood'),
        ('Storm', 'Storm'),
        ('Other', 'Other')
    )
    country = models.ForeignKey(Country)
    date = models.DateField('Date', blank=True, null=True)
    hazard_type = models.CharField('Hazard type', max_length=30, choices=HAZARD_TYPE_CHOICES)
    confidence = models.IntegerField('Confidence', blank = True, null=True, choices=CONFIDENCE_CHOICES)
    alert_level = models.CharField('Alert level', max_length=30, choices=EVENT_TYPE_CHOICES) 
    event_comment = models.TextField('Comment', blank=True)
    visible = models.BooleanField('Visible', blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return u'%s %s %s %s' % (self.country.terr_name, self.date, self.alert_level, self.hazard_type)
