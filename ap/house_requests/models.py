from django.db import models
import datetime

"""
The purpose of this module is to allow HC’s to submit linens requests for their respective house from a list of applicable items. They can specify the quantity of the item needed as well as provide a reason for needing a replacement. They should be able to request as many items as needed. The HC’s should be able to view a list of their active and fulfilled linens requests for their respective house. TA’s or serving sisters can view the list of active requests and can either mark requests as approved, denied, or partially denied requests.

If a request is denied or partially denied, a comment can be made by the person handling the request. This comment will be viewed as part of the notification sent to the HC who made the request.
"""
class LinensRequest(models.Model):

	REQUEST_STATUS = (
		('A',		'Approved'),
		('D',		'Denied'),
		('P',		'Partial')
	)

	ITEM = (
		('BAM',		'Bath Mat'),
		('BLT',		'Blanket'),
		('CMP',		'Cloth Matress Pad'),
		('COM',		'Comforter'),
		('DRM',		'Door Mat'),
		('FMP',		'Foam Matress Pad'),
		('FFS',		'Full Fitted Sheet'),
		('FFLS',	'Full Flat Sheet'),
		('HDT',		'Hand Towel'),
		('IBC',		'Ironing Board Cover'),
		('KFS',		'King Fitted Sheet'),
		('KFLS',	'King Flat Sheet'),
		('LSC',		'Love Seat Cover'),
		('PLW',		'Pillow'),
		('PLWC',	'Pillow Case'),
		('QFS',		'Queen Fitted Sheet'),
		('QFLS',	'Queen Flat Sheet'),
		('SHC',		'Shower Curtain'),
		('SHR',		'Shower Curtain Ring'),
		('SHRD',	'Shower Curtain Rod'),
		('SCC',		'Single Couch Cover'),
		('SLB',		'Sleeping Bag'),
		('TBC',		'Tablecloth'),
		('TWL',		'Towel'),
		('TSCC',	'Triple Seat Couch Cover'),
		('TFS',		'Twin Fitted Sheet'),
		('TFLS',	'Twin Flat Sheet'),
		('WSC',		'Washcloth')
	)

	REASON = (
		('STD', 'Stained'),
		('RWO', 'Ragged/Worn Out'),
		('TRN', 'Torn'),
		('MMP', 'Missing/Misplaced'),
		('OTR', 'OTHER')
	)

	date_requested = models.DateTimeField(auto_now_add=True)

	quantity = models.SmallIntegerField(default=1)

	status = models.CharField(max_length=1, choices=REQUEST_STATUS)

	item = models.CharField(max_length=4, choices=ITEM)

	reason = models.CharField(max_lenth=3, choices=REASON)

	def __unicode__(self):
		return u' %s' % (self.name)