from django.db import models
from django.contrib.gis.db import models
import datetime

class Country(models.Model):
	#id => automatically created
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


class Election(models.Model):
	country = models.ForeignKey(Country)
	election_date_start = models.DateField('Date (first round)', blank=True, null=True)
	election_date_text = models.CharField('Date (estimation)', max_length=25, blank=True, null=True)
	election_date_end = models.DateField('Date (second round)', blank=True, null=True)
	ELECTION_TYPE_CHOICES = (
		('Presidential', 'Presidential'),
		('Parliamentary', 'Parliamentary'),
		('Presidential / Parliamentary', 'Presidential / Parliamentary'),
		('Referendum', 'Referendum'),
		('Local Election', 'Local Election')
	)
	election_type = models.CharField('Type', max_length=30, choices=ELECTION_TYPE_CHOICES) 
	election_comment = models.TextField('Comment', blank=True)
	election_date_estimation = models.DateField('Date (estimation duplicated)', blank=True, null=True)

	# Returns the string representation of the model.
	def __unicode__(self):
		return u'%s %s %s' % (self.country.terr_name, self.election_date_start, self.election_type)


class Update(models.Model):
	election = models.ForeignKey(Election)
	update_date = models.DateField('Date')
	update_description = models.TextField('Comment', blank=True)
	update_source = models.URLField('Sources', max_length=500, blank=True, null=True)

	# Returns the string representation of the model.
	#def __unicode__(self):
	#    return self.update_date


