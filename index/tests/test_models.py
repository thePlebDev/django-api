from django.test import TestCase

from index.models import Songs

class SongsModelTest(TestCase):
	'''
		this is the models that will test the __str__ method on my model. I do not have to 
		test the individual fields on the model, because django does its own testing on them
	'''
	
	def setUp(self):
		#this sets up the object that will be used by all the objects
		Songs.objects.create(title = 'boby', artist ='this is how we do it')

	def test_str_model_method(self):
		# this grabs the frist song model and then tests to see if it works like it should
		song_one = Songs.objects.get(id=1)
		expected_result = f'{song_one.title} by {song_one.artist}'
		self.assertEquals(expected_result, str(song_one))

