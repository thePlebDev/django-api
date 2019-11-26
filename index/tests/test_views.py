from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from index.models import Songs
from .serializers import SongSerializer

#TEST FOR THE VIEWS

class BaseViewTest(APITestCase):
	'''
	 - inheriting from APITestCase, which is the restframework's version of TestCase form
	 django. APITestcase creates a clean database before the tests are run
	 - APIClient allows  us to simulate user interaction with the code at a view level
	 - If your tests do not need a database, inherit from APISimpleTestCase, this will
	 make the test run faster. Creation of the database will slow tests down
	 - when the test command is run any TestCase subclass will automatically build a test suite
	 out of those test cases and run that suit.

	'''
	client = APIClient
	#setting up the dummy client

	@staticmethod # static method saying that it doesnt need access to the instance method
	def create_song(title='',artist=''):
		if title != '' and artist != '': 
			'''
				the default arguments of title and artist seem to be a form of error handling?
				For if we pass it nothing it wont raise an error

			'''
			Songs.objects.create(title=title, artist=artist)
	'''
		- not sure if the method above is really necessary, we can just call
		Songs.objects.create in the setup method. Will check this out later
	'''

	def setUp(self):
		# called before every test funtion. Sets up the object to be tested
		self.create_song("like glue", "sean paul")
   

class GetAllSongsTest(BaseViewTest):

	def test_get_all_songs(self):
		'''
		this test ensures that all songs added in the setup method exist
		when we make a GET request to the songs/ endpoint
		'''

		#Hit the API endpoint
		response = self.client.get(
			reverse('songs-all',kwargs={'version': 'v1'})
			)

		#fetch the data from db
		expected = Songs.objects.all()
		serialized = SongSerializer(expected,many=True)
		self.assertEqual(response.data,serialized.data)
		self.assertEqual(response.status_code, 200)