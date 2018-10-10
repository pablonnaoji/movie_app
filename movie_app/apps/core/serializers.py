from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		fields = ('id', 'title', 'rating', 'plot', 'genre' ,'release_date',)
		model = models.Movie