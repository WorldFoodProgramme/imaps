from django.test import TestCase
from odep.models import *
from django.test.client import Client
import json

class EventTest(TestCase):
	fixtures = ['test_data.json',]
	
	def testPostRequestReturns403(self):
		c = Client()
		resp = c.post('/report/odep/2009/03')
		self.assertEqual(resp.status_code,403)
	
	def testSuccessMapCopyWithUnitYearMonth(self):
		"""
		Test that a request done with unit, year and month returns a 200 status
		"""
		c = Client()
		resp = c.get('/report/odep/2009/03')
		self.assertEqual(resp.status_code,200)
		
	def testSuccessMapCopyWithUnitYear(self):
		"""
		Test that a request done with unit and year returns a 200 status
		"""
		c = Client()
		resp = c.get('/report/odep/2009')
		self.assertEqual(resp.status_code,200)
	
	def testSuccessMapCopyWithUnit(self):
		"""
		Test that a request done with unit returns a 200 status
		"""
		c = Client()
		resp = c.get('/report/odep')
		self.assertEqual(resp.status_code,200)
		
	def testSuccessMapCopyWithYear(self):
		"""
		Test that a request done with year returns a 200 status
		"""
		c = Client()
		resp = c.get('/report/2012')
		self.assertEqual(resp.status_code,200)
		
	def testSuccessMapCopyWithYearMonth(self):
		"""
		Test that a request done with year and month returns a 200 status
		"""
		c = Client()
		resp = c.get('/report/2012/1')
		self.assertEqual(resp.status_code,200)
		
	def testReportMapCopyWithUnitYearMonth(self):
		"""
		Test that a request done with unit, year and month returns the correct content 
		"""
		c = Client()
		resp = c.get('/report/odep/2012/01')
		self.assertTrue('horn' in resp.content)
		
	def testReportMapCopyWithUnitYear(self):
		"""
		Test that a request done with unit and year returns the correct content 
		"""
		c = Client()
		resp = c.get('/report/odep/2012')
		self.assertTrue('horn' in resp.content)
		
	def testReportMapCopyWithUnit(self):
		"""
		Test that a request done with unit returns the correct content 
		"""
		c = Client()
		resp = c.get('/report/odep')
		self.assertTrue('horn' in resp.content)
		
	def testReportMapCopyWithYear(self):
		"""
		Test that a request done with year returns the correct content 
		"""
		c = Client()
		resp = c.get('/report/2012')
		self.assertTrue('horn' in resp.content)
		
	def testReportMapCopyWithYearMonth(self):
		"""
		Test that a request done with year and month returns the correct content 
		"""
		c = Client()
		resp = c.get('/report/2012/1')
		self.assertTrue('horn' in resp.content)
		
	def testUnitHasCorrectNumberOfCopies(self):
		"""
		Test that the total nomber of printed maps for odep is 6
		"""
		c = Client()
		resp = c.get('/report/odep')
		jsonresponse = json.loads(resp.content)
		num = 0
		for mapcopy in jsonresponse['items']:
			num+=mapcopy['copies']
		self.assertEqual(num,6)
		
	def testUnitHasCorrectNumberOfCopiesPerYear(self):
		"""
		Test that the total nomber of printed maps for odep in 2012 is 6
		"""
		c = Client()
		resp = c.get('/report/odep/2012')
		jsonresponse = json.loads(resp.content)
		num = 0
		for mapcopy in jsonresponse['items']:
			num+=mapcopy['copies']
		self.assertEqual(num,6)
		
	def testYearHasCorrectNumberOfCopies(self):
		"""
		Test that the total nomber of printed maps for 2012 is 12
		"""
		c = Client()
		resp = c.get('/report/2012')
		jsonresponse = json.loads(resp.content)
		num = 0
		for mapcopy in jsonresponse['items']:
			num+=mapcopy['copies']
		self.assertEqual(num,12)
		
	def testYearMonthHasCorrectNumberOfCopies(self):
		"""
		Test that the total nomber of printed maps for 2012/1 is 12
		"""
		c = Client()
		resp = c.get('/report/2012/1')
		jsonresponse = json.loads(resp.content)
		num = 0
		for mapcopy in jsonresponse['items']:
			num+=mapcopy['copies']
		self.assertEqual(num,12)
		
	def testFebruaryHasNoCopies(self):
		"""
		Test that the total nomber of printed maps for 2012/2 is 12
		"""
		c = Client()
		resp = c.get('/report/2012/2')
		jsonresponse = json.loads(resp.content)
		num = 0
		for mapcopy in jsonresponse['items']:
			num+=mapcopy['copies']
		self.assertEqual(num,0)