from django.test import Client
from django.urls import reverse

from django.test import TestCase

from .models import Trainer
from trainer.forms import TrainerForm
import datetime

# Create your tests here.

class AddTrainerTestCase(TestCase):
	def setUp(self):
		self.data = {"first_name":"Nyandia",
					 "last_name":"Kamawe",
					 "gender":"Female",
					 "email":"graphicdesign@akirachix.com",
					 "phone_number":"0706823329",
					 "trainer_number":"B678",
					 "date_joined":datetime.date.today(),
					 "course_teaching":"Graphic Design"
					}

		self.bad_data = {"first_name":"Nyandia",
					 	 "last_name":"Kamawe",
					 	 "gender":"Female",
					 	 "email":"graphicdesignkirachix.com",
					 	 "phone_number":"07066823329",
					 	 "trainer_number":"B678",
					 	 "date_joined":datetime.date.today(),
					 	 "course_teaching":"Graphic Design"
					 	}

	def test_teacher_form_accepts_valid_data(self):
		form = TrainerForm(self.data)
		self.assertTrue(form.is_valid())

	def test_teacher_form_rejects_invalid_data(self):
		form = TrainerForm(self.bad_data)
		self.assertFalse(form.is_valid())


	def test_add_trainer_view(self):
		client = Client() 
		url = reverse("add_trainer") 
		response = client.post(url,self.data)
		self.assertEqual(response.status_code,200)


	def test_add_student_view_with_invalid_data(self):
		client = Client() 
		url = reverse("add_trainer") 
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code,400)

