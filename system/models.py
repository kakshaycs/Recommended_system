from django.db import models
import uuid

# Create your models here.
class USER(models.Model):
	userid = models.IntegerField()
	A = models.FloatField()
	B = models.FloatField()
	C = models.FloatField()
	D = models.FloatField()
	E = models.FloatField()

	def __str__(self):
		return str(self.userid);

class MOVIE(models.Model):
	movieid = models.IntegerField()
	A = models.FloatField()
	B = models.FloatField()
	C = models.FloatField()
	D = models.FloatField()
	E = models.FloatField()

	def __str__(self):
		return str(self.movieid);