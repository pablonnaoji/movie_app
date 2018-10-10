# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=50)
	rating = models.CharField(max_length=4)
	plot = models.TextField()
	genre = models.CharField(max_length=50)
	release_date = models.DateTimeField()

	def __str__(self):
		return self.title
