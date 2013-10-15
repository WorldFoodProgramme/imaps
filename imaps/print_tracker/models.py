from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class Map(models.Model):
	"""
	Database model for the Map entity
	"""
	title = models.CharField(max_length=128)
	file_name = models.CharField('Map num',max_length=128)
	date_completed = models.DateField()
	last_updated = models.DateField()
	type = models.CharField(max_length=20,blank=True,null=True)	
	status = models.CharField(max_length=1,choices=(('c','Completed'),('d','Draft')))
	up_odep = models.BooleanField('Uploaded to ODEP-GIS repository')
	up_back = models.BooleanField('Uploaded to ODEP backup hard drive')
	up_epweb = models.BooleanField('Uploaded to EP-WEB map repository')
	up_vam = models.BooleanField('Uploaded to VAM SIE')
	print_format = models.ForeignKey('Format')
	author_contact = models.CharField(max_length=25,blank=True,null=True)
	remarks = models.TextField(blank=True,null=True)
	
	def __unicode__(self):
		return self.title
	
class Format(models.Model):
	"""
	Database model for the Format entity
	"""
	name = models.CharField(max_length=2)
	cost = models.FloatField(null=True)
	
	def __unicode__(self):
		return self.name
		
class Copy(models.Model):
	"""
	Database model for the Copy entity
	"""
	map = models.ForeignKey('Map')
	format = models.ForeignKey('Format')
	number = models.IntegerField()
	requested_by = models.ForeignKey('Unit')
	
	class Meta:
		verbose_name_plural = 'Copies'
		
	def __unicode__(self):
		return self.map.title
	
	def save(self):
		"""
		Override of the save method used for storing MapCopy events and also to control that the number of copies is never decreased
		"""
		copies = Copy.objects.filter(map=self.map,format=self.format,requested_by=self.requested_by)
		number = copies[0].number if len(copies) > 0 else None
		if number is not None:
			pre_obj = self
			if pre_obj.number < number:
				raise ValidationError('Decrease the number of copies is not permitted')
			elif number == pre_obj.number:
				super(Copy,self).save()
			else:
				MapCopy(copy=self,number=pre_obj.number-number,unit=self.requested_by).save()
				super(Copy,self).save()
		else:
			super(Copy,self).save()
			MapCopy(copy=self,number=self.number,unit=self.requested_by).save()
		
	def getCost(self):
		return self.format.cost + settings.MAP_COST

class Unit(models.Model):
	"""
	Database model for the Unit entity
	"""
	name = models.CharField(max_length=128,blank=True,null=True)
	focal_point = models.CharField(max_length=128,blank=True,null=True)
	
	def __unicode__(self):
		return self.name
		
class MapCopy(models.Model):
	"""
	Database model for the MapCopy event.
	This hidden table is used as an archieve of all the print action performed
	"""
	date = models.DateField(auto_now=True)
	copy = models.ForeignKey('Copy')
	number = models.IntegerField()
	unit = models.ForeignKey('Unit')
	
	def __unicode__(self):
		return self.date.ctime()