from django.test import TestCase
from trainer.models import Trainer
from course.models import Course
import datetime



class TrainerCourseTestCase(TestCase):
	def setUp(self):
		self.trainer_a = Trainer.objects.create (
			first_name = "Kellie",
			last_name = "Murungi",
			gender = "female",
			email = "kelli@akirachix.com",
			course_teaching = "entrepreneurship",
			date_joined = datetime.date.today(),
			)

		self.trainer_b = Trainer.objects.create (
			first_name = "James",
			last_name = "Mwai",
			gender = "male",
			email = "Mwaimail@mail.com",
			course_teaching = "python, intro_to_computer",
			date_joined = datetime.date.today(),
			)

		self.course = Course.objects.create (
			name = "python",
			duration_in_months = 10,
			start_date = datetime.date.today(),
			end_date = datetime.date.today(),
			description = "Programming language. I enjoy using Django and coming up with new projects",
			)

		self.course = Course.objects.create (
			name = "entrepreneurship",
			duration_in_months = 10,
			start_date = datetime.date.today(),
			end_date = datetime.date.today(),
			description = " It's about coming up with business ideas, knowing how to work with your idea to get your product-market-fit and knowing and understanding one's target market. Business skills come in handy too.",
			)

		self.course = Course.objects.create (
			name = "graphic_design",
			duration_in_months = 10,
			start_date = datetime.date.today(),
			end_date = datetime.date.today(),
			description = " This is where one's creativity comes to action. Coming up with logos, using photoshop, working on Adobe illustrator, using InDesign and many more. It's the most exciting and interesting course for me",
			)

	def test_many_courses_can_be_trained_by_one_trainer(self):
	   self.trainer_a.python = self.trainer_b
	   self.intro_to_computer.trainer = self.trainer_b
	   self.assertEqual(self.intro_to_computer.trainer,self.python.trainer)


	def test_one_course_can_be_trained_by_a_trainer(self):
	   self.python.trainer = self.trainer_a
	   self.assertEqual(self.python.trainer, self.trainer_a)


