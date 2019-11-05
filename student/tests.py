# test code
from django.test import Client
from django.urls import reverse
from student.forms import StudentForm

from django.test import TestCase
from .models import Student
import datetime

class StudentTestCase (TestCase):
	def setUp(self):
		self.student = Student (
			first_name = "Sharon",
			last_name = "Akoth",
			date_of_birth = datetime.date(1997,11,12),
			gender = "female",
			registration_number = "123",
			email = "akothsharon19@gmail.com",
			phone_number = "072574757",
			date_joined = datetime.date.today(),
			)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

	def test_age_is_always_above_18(self):
		self.assertFalse(self.student.clean() < 18 )

	def test_age_is_always_below_40(self):
		self.assertFalse(self.student.clean() > 40 )


class AddStudentTestCase(TestCase):
	def setUp(self):
		self.data = {"first_name":"Sharon",
					 "last_name":"Akoth",
					 "gender":"female",
					 "date_of_birth":datetime.date(1997,11,12),
					 "email":"akothsharon19@gmail.com",
					 "phone_number":"072574657",
					 "registration_number":"123",
					 "date_joined":datetime.date.today(),
					 }

		self.bad_data = {"first_name":"Sharon",
					 	 "last_name":"Akoth",
					 	 "gender":6,
					 	 "date_of_birth":datetime.date(1,11,12),
					 	 "email":"akothsharon19@gmail.com",
					 	 "phone_number":"awgr",
					 	 "registration_number":"112",
					 	 "date_joined":datetime.date.today(),
					 	}


	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())


	def test_add_student_view(self):
		client = Client() 
		url = reverse("add_student") 
		response = client.post(url,self.data)
		self.assertEqual(response.status_code,200)

	def test_add_student_view_with_invalid_data(self):
		client = Client() 
		url = reverse("add_student") 
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code,400)


# Create your tests here.
