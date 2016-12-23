from __future__ import unicode_literals

from django.db import models



class book_db(models.Model):
	title = models.CharField(max_length=100)
	link = models.CharField(max_length=500)
	date = models.DateField()

	def __str__(self):
		return self.title