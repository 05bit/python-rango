# -*- coding: utf-8 -*-
from unidecode import unidecode
from rango import crypto

def safe_filename(name):
	return unidecode(name)

def safe_upload_to(prefix='', pattern=None, random_size=20):
	"""
	This helper provides collision-safe and some kind secure
	file path maker, which can be used for ``upload_to``
	parameter.

	Non-ASCII chars will be converted to ASCII, random token
	and instance pk will be used by default for constructing
	full path for uploading.

	Example::

		class MyModel(models.Model):
			file = models.FileField(upload_to=safe_upload_to('files'))
	"""
	pattern = pattern or '%(prefix)s/%(pk)s/%(random)s_%(name)s'
	bits = {}
	if '(prefix)' in pattern:
		bits['prefix'] = prefix or '_'
	def upload_to(instance, name):
		bits['pk'] = instance.pk or -1
		if '(random)' in pattern:
			bits['random'] = crypto.random_token(random_size)
		if '(name)' in pattern:
			bits['name'] = safe_filename(name)
		return pattern % bits
	return upload_to