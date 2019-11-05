from django.test import Client
from django.urls import reverse

from django.test import TestCase
from .models import Course
from course.forms import CourseForm
import datetime

# Create your tests here.


class AddCourseTestCase(TestCase):
	def setUp(self):
		self.data = {"name":"Python",
					 "duration_in_months":10,
					 "start_date":datetime.date.today(),
					 "end_date":datetime.date.today(),
					 "description":"Programming language. I enjoy using Django and coming up with new projects",
					}

		self.bad_data = {"name":45,
						 "duration_in_months":"er",
						 "start_date":datetime.date.today(),
						 "end_date":datetime.date.today(),
						 "description":"Programming language. I enjoy using Django and coming up with new projects",
						 }

	
	def test_course_form_accepts_valid_data(self):
		form = CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form = CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())


	def test_add_course_view_data(self):
		client = Client() 
		url = reverse("add_course") 
		response = client.post(url,self.data)
		self.assertEqual(response.status_code,200) 


	def test_add_student_view_with_invalid_data(self):
		client = Client() 
		url = reverse("add_course") 
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code,400)
